import re

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from scipy.stats import rankdata

import kbo2023all  # KBO
import kbo_2023_html  # livesport
import pm10
import weather
from holi import dfholi

### html file 불러오기 ####
# livesport data
html = kbo_2023_html.html
soup = BeautifulSoup(html, "html.parser")

# Initialize empty lists to store data
dates = []
homes = []
aways = []
home_scores = []
away_scores = []
home_pitchers = []
away_pitchers = []
pitchers = []

# Loop through each relevant div
for div in soup.find_all("div", class_="event__match"):
    date = div.select_one(".event__time").text.strip()
    home = div.select_one(".event__participant--home").text.strip()
    away = div.select_one(".event__participant--away").text.strip()
    home_score = div.select_one(".event__score--home").text.strip()
    away_score = div.select_one(".event__score--away").text.strip()
    try:
        pitcher = div.select_one(".event__pitchers").text.strip()
    except:
        pitcher = None

    # Append data to lists
    dates.append(date)
    homes.append(home)
    aways.append(away)
    home_scores.append(home_score)
    away_scores.append(away_score)
    pitchers.append(pitcher)

# 투수 1, 2 뽑기 위한 필터 설정
pattern = re.compile(r"\[.*?\]|\(.*?\)|투수:|승:|패:")
temp = []
# 필터로 거르기
for pitcher in pitchers:
    if pitcher != None:
        cleaned_data = pattern.sub("", pitcher)
        cleaned_data = cleaned_data.split(",")
        temp.append(cleaned_data)
    else:
        temp.append(None)
# 스트립 과정
for sublist in temp:
    if sublist != None:
        for i, element in enumerate(sublist):
            sublist[i] = element.strip()

temp1 = []
temp2 = []
for i in temp:
    if i != None:
        temp1.append(i[0])
        try:
            temp2.append(i[1])
        except:
            temp2.append(None)
    else:
        temp1.append(None)
        temp2.append(None)

# Create a DataFrame
data = {
    "date": dates,
    "home": homes,
    "away": aways,
    "home_score": home_scores,
    "away_score": away_scores,
    "pitcher1": temp1,
    "pitcher2": temp2,
}
df = pd.DataFrame(data)

df["time"] = df["date"].str.split().str[1]
df["date"] = df["date"].str.split().str[0]
# print(df)

# data type change to numeric
df["home_score"] = df["home_score"].apply(pd.to_numeric, errors="coerce")
df["away_score"] = df["away_score"].apply(pd.to_numeric, errors="coerce")

# Add columns with team names
team_columns = ["LG", "KT", "SSG", "NC", "두산", "KIA", "롯데", "삼성", "한화", "키움"]
df[team_columns] = 0

### 경기 순서 역순 만들기 ###
df = df[::-1]

### date format 통일 ###

date = df["date"].tolist()
new_date = []
for i in date:
    temp = "2023" + i[3:5] + i[0:2]
    new_date.append(temp)

df["date"] = new_date

### 정규리그만 가져오기 ###
df["date"] = df["date"].apply(pd.to_numeric, errors="coerce")
df_filtered = df[(df.date >= 20230401) & (df.date <= 20231018)]
df_filtered.index = range(len(df_filtered))
df = df_filtered
# print(df)

### team 누적 승리 계산 ###
dic = {}
for i in team_columns:
    dic[i] = 0
for i, row in df.iterrows():
    home = row["home"]
    away = row["away"]
    home_score = row["home_score"]
    away_score = row["away_score"]
    if home_score > away_score:
        dic[home] += 1
    elif away_score > home_score:
        dic[away] += 1
    else:
        pass
    for team in team_columns:
        df.at[i, team] = dic[team]

# print(df)
### 누적 승리에 따른 랭킹 만들기 ###
team_ranks = [
    "LG_rank",
    "KT_rank",
    "SSG_rank",
    "NC_rank",
    "두산_rank",
    "KIA_rank",
    "롯데_rank",
    "삼성_rank",
    "한화_rank",
    "키움_rank",
]
df_part2 = pd.DataFrame(columns=team_ranks, index=df.index)
# print(df_part2)

for idx, i in enumerate(df.values):
    wins = i[8:]
    # Use rankdata to assign ranks
    ranks = rankdata(wins, method="min")

    # Convert ranks to integers
    ranks = (ranks.max() + 1) - ranks.astype(int)

    # Display the result
    df_part2.loc[idx] = ranks

merged_df = pd.concat([df, df_part2], axis=1)

### group당 ranking, 그날 순위 다음에 넘기고 초반엔 5로 고정 ###
# Set the default value for the first group
default_value = 5

# Iterate over the groups and update the values
for column in team_ranks:
    prev_value = default_value
    for _, group in merged_df.groupby("date"):
        merged_df.loc[group.index, column] = prev_value
        prev_value = group[column].iloc[-1]

### give home_rank and away_rank ###

for i in range(len(merged_df)):
    home = merged_df.loc[i, "home"]
    away = merged_df.loc[i, "away"]
    merged_df.loc[i, "home_rank"] = merged_df.loc[i, f"{home}_rank"]
    merged_df.loc[i, "away_rank"] = merged_df.loc[i, f"{away}_rank"]

### insert holidays ###
holis = dfholi["locdate"].tolist()
holi_lst = []
for i in holis:
    holi_lst.append(i)

merged_df["공휴일"] = np.where(merged_df["date"].isin(holi_lst), 1, 0)
# print(merged_df)

### expected_score ###
team_columns = ["LG", "KT", "SSG", "NC", "두산", "KIA", "롯데", "삼성", "한화", "키움"]

dic = {}
for team in team_columns:
    df = pd.DataFrame(columns=["date", "team", "score"])
    for idx, i in enumerate(merged_df.values):
        if i[1] == team:
            df.loc[idx] = [i[0], i[1], i[3]]

        if i[2] == team:
            df.loc[idx] = [i[0], i[2], i[4]]
    df["ex_score"] = df["score"].rolling(window=5).mean().shift(1)
    df["index"] = df.index
    dic[team] = df
    # print(df)

##########여기까지 괜찮아~###############
### expected score clear!, with fillna(5) ###
merged_df["index"] = merged_df.index

for team in team_columns:
    merged_df = pd.merge(
        merged_df,
        dic[team],
        # left_index=True,
        left_on=["date", "home", "home_score", "index"],
        right_on=["date", "team", "score", "index"],
        # right_index=True,
        how="left",
        suffixes=("", f"_home_{team}"),
    )
    merged_df = merged_df.drop(columns=["team", "score"])

for team in team_columns:
    merged_df = pd.merge(
        merged_df,
        dic[team],
        # left_index=True,
        left_on=["date", "away", "away_score", "index"],
        right_on=["date", "team", "score", "index"],
        # right_index=True,
        how="left",
        suffixes=["", f"_away_{team}"],
    )
    merged_df = merged_df.drop(columns=["team", "score"])

##########

merged_df["merged_ex_score"] = (
    merged_df["ex_score"]
    .fillna(merged_df["ex_score_home_KT"])
    .fillna(merged_df["ex_score_home_SSG"])
    .fillna(merged_df["ex_score_home_NC"])
    .fillna(merged_df["ex_score_home_두산"])
    .fillna(merged_df["ex_score_home_KIA"])
    .fillna(merged_df["ex_score_home_롯데"])
    .fillna(merged_df["ex_score_home_삼성"])
    .fillna(merged_df["ex_score_home_한화"])
    .fillna(merged_df["ex_score_home_키움"])
    .fillna(5)
)
merged_df["merged_ex_score_away"] = (
    merged_df["ex_score_away_LG"]
    .fillna(merged_df["ex_score_away_KT"])
    .fillna(merged_df["ex_score_away_SSG"])
    .fillna(merged_df["ex_score_away_NC"])
    .fillna(merged_df["ex_score_away_두산"])
    .fillna(merged_df["ex_score_away_KIA"])
    .fillna(merged_df["ex_score_away_롯데"])
    .fillna(merged_df["ex_score_away_삼성"])
    .fillna(merged_df["ex_score_away_한화"])
    .fillna(merged_df["ex_score_away_키움"])
    .fillna(5)
)
# print(merged_df)

# ### everything i want ###
selected_columns = [
    "date",
    "home",
    "away",
    "home_score",
    "away_score",
    "home_rank",
    "away_rank",
    "공휴일",
    "merged_ex_score",
    "merged_ex_score_away",
    "pitcher1",
    "pitcher2",
    "time",
]
new_df = merged_df[selected_columns]
# new_df.to_csv('plsgod4.csv')

# KBO data
df2023 = pd.read_html(kbo2023all.html)[0]
# df2023 = df2023[:-1]
df2023 = df2023.drop(df2023.index[-1])
# print(df2023)
lst_temp = []
for i in df2023["날짜"]:
    i = i[0:4] + i[5:7] + i[8:]
    lst_temp.append(int(i))
df2023["날짜"] = lst_temp

grouped_df1 = new_df.groupby("date")
df1 = pd.DataFrame()
for i in grouped_df1:
    i = i[1].sort_values(by="home", ascending=True)
    df1 = pd.concat([df1, i])
df1.index = range(720)
# print(df1)

grouped_df2 = df2023.groupby("날짜")
df2 = pd.DataFrame()
for i in grouped_df2:
    i = i[1].sort_values(by="홈", ascending=True)
    df2 = pd.concat([df2, i])
df2.index = range(720)
# print(df2)

merged_df = pd.merge(df1, df2, left_index=True, right_index=True, how="left")
merged_df = merged_df.drop(columns=["날짜", "홈", "방문"])
# print(merged_df)


################# 날씨 추가 ##############
# temp_df = weather.temp_df
# rain_df = weather.rain_df

merged_df.to_csv("temp2023_1.csv")
# print(merged_df)
