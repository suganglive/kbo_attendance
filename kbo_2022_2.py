import numpy as np
import pandas as pd

import pm10
import weather

df = pd.read_csv("./data/temp2022_1.csv", index_col=0)

# 영어이름으로 바꾸기
dic = {
    "롯데": "Lotte",
    "두산": "Doosan",
    "한화": "Hanhwa",
    "삼성": "Samsung",
    "키움": "Kiwoom",
}
for i in dic:
    #     print(i, dic[i])
    df.replace(f"{i}", f"{dic[i]}", inplace=True)

# 월 column 만들기
lst = []
for i in df["date"]:
    i = str(i)
    i = i[4:6]
    lst.append(i)
df["month"] = lst

# year column 만들기
lst = []
for i in df["date"]:
    i = str(i)
    i = i[0:4]
    lst.append(i)
df["year"] = lst

df["first_game"] = np.where(df["date"] == (20230401 or 20220401), 1, 0)

# 강수량
rain_df = weather.rain_df

dic = {
    "SSG": "인천연수",
    "NC": "마산회원",
    "Samsung": "경산",
    "KIA": "풍암",
    "LG": "송파",
    "Hanhwa": "오월드",
    "KT": "의왕",
    "Kiwoom": "광명",
    "Lotte": "동래",
    "Doosan": "송파",
}

rain_df["date"] = rain_df.index
rain_df["date2"] = pd.to_numeric(rain_df["date"], errors="coerce")

merged_df = pd.merge(df, rain_df, left_on="date", right_on="date2", how="left")
df = merged_df

for idx, row in df.iterrows():
    home = row["home"]
    df.loc[idx, "rain"] = row[dic[home]]

lst = list(rain_df.columns)
lst.append("date_y")
lst.remove("date")
df.drop(columns=lst, inplace=True)


df["date"] = df["date_x"]
df = df.drop(columns="date_x")

# temperture
temp_df = weather.temp_df

dic = {
    "SSG": "인천연수",
    "NC": "마산회원",
    "Samsung": "경산",
    "KIA": "풍암",
    "LG": "송파",
    "Hanhwa": "오월드",
    "KT": "의왕",
    "Kiwoom": "광명",
    "Lotte": "동래",
    "Doosan": "송파",
}

temp_df["date"] = temp_df.index
temp_df["date2"] = pd.to_numeric(temp_df["date"], errors="coerce")

merged_df = pd.merge(df, temp_df, left_on="date", right_on="date2", how="left")
df = merged_df

for idx, row in df.iterrows():
    home = row["home"]
    df.loc[idx, "temp"] = row[dic[home]]

lst = list(temp_df.columns)
lst.append("date_y")
lst.remove("date")
df.drop(columns=lst, inplace=True)

df["date"] = df["date_x"]
df = df.drop(columns="date_x")


# pm10
pm10_df = pm10.df

dic = {
    "SSG": "서울",
    "NC": "구덕산",
    "Samsung": "대구",
    "KIA": "광주",
    "LG": "서울",
    "Hanhwa": "천안",
    "KT": "수원",
    "Kiwoom": "서울",
    "Lotte": "구덕산",
    "Doosan": "서울",
}

# pm10_df['date'] = pm10_df.index
pm10_df["date2"] = pd.to_numeric(pm10_df["date"], errors="coerce")
merged_df = pd.merge(df, pm10_df, left_on="date", right_on="date2", how="left")
df = merged_df

for idx, row in df.iterrows():
    home = row["home"]
    df.loc[idx, "pm10"] = row[dic[home]]

lst = list(pm10_df.columns)
lst.append("date_y")
lst.remove("date")
df.drop(columns=lst, inplace=True)

df["date"] = df["date_x"]
df = df.drop(columns="date_x")

# df.to_csv('temp7.csv')
# pm10_df.to_csv('pm7.csv')

# before_attendance
dic = {
    "SSG": "인천연수",
    "NC": "마산회원",
    "Samsung": "경산",
    "KIA": "풍암",
    "LG": "송파",
    "Hanhwa": "오월드",
    "KT": "의왕",
    "Kiwoom": "광명",
    "Lotte": "동래",
    "Doosan": "송파",
}
teams = list(dic)
grouped_df = df.groupby("home")
# print(grouped_df)
modified_groups = []
for group in grouped_df:
    # print(group[1])
    group[1]["before_attendance"] = group[1]["관중수"].shift(1)
    # df['ex_score'] = df['score'].rolling(window=5).mean().shift(1)
    group[1]["before_5game_avg"] = group[1]["관중수"].rolling(window=5).mean().shift(1)
    # Specify the columns you want to fill with the mean
    columns_to_fill = ["before_attendance", "before_5game_avg"]

    # Calculate the mean of the selected columns
    column_means = group[1]["관중수"].mean()

    # Fill missing values in the selected columns with the mean
    group[1][columns_to_fill] = group[1][columns_to_fill].fillna(column_means)

    # 상대 전적(직전, 최근 5경기)
    # gg_df = group[1].groupby('away')
    # mm_groups = []
    # for g in gg_df:
    #     # if g[1]['home_score'] > g[1]['away_score']:
    #     #     g[1]['before_match'] = 'win'
    #     # elif g[1]['home_score'] < g[1]['away_score']:
    #     #     g[1]['before_match'] = 'lose'
    #     # else:
    #     #     g[1]['before_match'] = 'even'
    #     g[1]['before_match'] = np.where(g[1]['home_score'] > g[1]['away_score'], 'win',
    #                                  np.where(g[1]['home_score'] < g[1]['away_score'], 'lose', 'even'))
    #     g[1]['before_match'] = g[1]['before_match'].shift(1)
    #     # g[1].to_csv('temp10.csv')
    #     mm_groups.append(g[1])
    # new_df = pd.concat(mm_groups)

    # modified_groups.append(new_df)
    modified_groups.append(group[1])
merged_df = pd.concat(modified_groups)
merged_df.sort_index(inplace=True)
df = merged_df
# print(df)
# Assuming df is your DataFrame
# Filter rows where 'home' or 'away' is 'KT' or 'LG'
# print(len(teams))

# last match
temp_list = []
a = 0
for team in teams:
    for t in teams:
        filtered_df = df[
            df["home"].isin([f"{team}", f"{t}"]) & df["away"].isin([f"{team}", f"{t}"])
        ]
        filtered_df["last_match"] = np.where(
            filtered_df["home_score"] > filtered_df["away_score"],
            "win",
            np.where(
                filtered_df["home_score"] < filtered_df["away_score"], "lose", "even"
            ),
        )
        filtered_df["last_match"] = filtered_df["last_match"].shift(1)
        filtered_df["last_match"] = filtered_df["last_match"].fillna("even")
        print(filtered_df)
        temp_list.append(filtered_df)
    teams.remove(team)
    # teams.append(team)
    # print('team complete')
    # a += 1
    # print(f'{a}/10')
    # print(teams)
for team in teams:
    for t in teams:
        filtered_df = df[
            df["home"].isin([f"{team}", f"{t}"]) & df["away"].isin([f"{team}", f"{t}"])
        ]
        filtered_df["last_match"] = np.where(
            filtered_df["home_score"] > filtered_df["away_score"],
            "win",
            np.where(
                filtered_df["home_score"] < filtered_df["away_score"], "lose", "even"
            ),
        )
        filtered_df["last_match"] = filtered_df["last_match"].shift(1)
        filtered_df["last_match"] = filtered_df["last_match"].fillna("even")
        print(filtered_df)
        temp_list.append(filtered_df)
    teams.remove(team)
    # print(teams)
filtered_df = df[
    df["home"].isin([f"KIA", f"Kiwoom"]) & df["away"].isin([f"KIA", f"Kiwoom"])
]
filtered_df["last_match"] = np.where(
    filtered_df["home_score"] > filtered_df["away_score"],
    "win",
    np.where(filtered_df["home_score"] < filtered_df["away_score"], "lose", "even"),
)
filtered_df["last_match"] = filtered_df["last_match"].shift(1)
filtered_df["last_match"] = filtered_df["last_match"].fillna("even")
temp_list.append(filtered_df)

merged_df = pd.concat(temp_list)
merged_df.sort_index(inplace=True)
# merged_df.to_csv('temp15.csv')
merged_df.to_csv("./data/temp2022_2.csv")
# print(merged_df)

# # df 초기화, win, lose, even 숫자화
# df = merged_df
# df['last_match_num'] = np.where(df['last_match'] == 'win', 1,
#                                  np.where(df['last_match'] == 'lose', -1, 0))

# ## 직전 3경기 ##
# teams = list(dic)
# for team in teams:
#     for t in teams:
#         filtered_df = df[df['home'].isin([f'{team}', f'{t}']) & df['away'].isin([f'{team}', f'{t}'])]
#         filtered_df['last_3_match'] = df['last_match_num'].rolling(window=3).sum()
#         # print(filtered_df)
#         temp_list.append(filtered_df)
#     teams.remove(team)
# Display the result
# print(filtered_df)


# for team in teams:
# grouped_df = df.groupby('team')
# df['before_attendance'] =

# # Add columns of pitchers
# ps = []
# for i, r, in df.iterrows():
#     p1 = r['pitcher1']
#     p2 = r['pitcher2']
#     print(p1, p2)
#     ps.append(p1)
#     ps.append(p2)
# ps = list(set(ps))

# df[ps] = 0

# ### team 누적 승리 계산 ### 가져올때부터 홈, away로 가져와야함.
# dic = {}
# for i in team_columns:
#     dic[i] = 0
# for i, row in df.iterrows():
#     home = row['home']
#     away = row['away']
#     home_score = row['home_score']
#     away_score = row['away_score']
#     if home_score > away_score:
#         dic[home] += 1
#     elif away_score > home_score:
#         dic[away] += 1
#     else:
#         pass
#     for team in team_columns:
#         df.at[i, team] = dic[team]
