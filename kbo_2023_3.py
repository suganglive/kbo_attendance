import numpy as np
import pandas as pd

df = pd.read_csv("./data/temp2023_2.csv", index_col=0)

# print(df)

# 피타고리안 기대 승률
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

for team in teams:
    df[f"{team}_누적득점"] = 0
    df[f"{team}_누적실점"] = 0

for idx, row in df.iterrows():
    # print(idx)
    home = row["home"]
    away = row["away"]
    if idx == 0:
        df.loc[idx, f"{home}_누적득점"] = row["home_score"]
        df.loc[idx, f"{home}_누적실점"] = row["away_score"]
        df.loc[idx, f"{away}_누적득점"] = row["away_score"]
        df.loc[idx, f"{away}_누적실점"] = row["home_score"]
    else:
        df.loc[idx, f"{home}_누적득점"] = (
            row["home_score"] + df.loc[idx - 1, f"{home}_누적득점"]
        )
        df.loc[idx, f"{home}_누적실점"] = (
            row["away_score"] + df.loc[idx - 1, f"{home}_누적실점"]
        )
        df.loc[idx, f"{away}_누적득점"] = (
            row["away_score"] + df.loc[idx - 1, f"{away}_누적득점"]
        )
        df.loc[idx, f"{away}_누적실점"] = (
            row["home_score"] + df.loc[idx - 1, f"{away}_누적실점"]
        )
    teams.remove(home)
    teams.remove(away)
    for team in teams:
        if idx != 0:
            df.loc[idx, f"{team}_누적득점"] = df.loc[idx - 1, f"{team}_누적득점"]
            df.loc[idx, f"{team}_누적실점"] = df.loc[idx - 1, f"{team}_누적실점"]
    teams.append(home)
    teams.append(away)

# df.to_csv('temp17.csv')
for idx, row in df.iterrows():
    home = row["home"]
    df.loc[idx, "pythagorean_expectation"] = (row[f"{home}_누적득점"] ** 2) / (
        (row[f"{home}_누적득점"] ** 2) + (row[f"{home}_누적실점"] ** 2)
    )

# df.to_csv('temp21.csv')

grouped = df.groupby("home")
modified_groups = []
for g in grouped:
    g[1]["pythagorean_expectation"] = g[1]["pythagorean_expectation"].shift(1)
    modified_groups.append(g[1])

merged_df = pd.concat(modified_groups)
merged_df.sort_index(inplace=True)
df = merged_df
df["pythagorean_expectation"] = df["pythagorean_expectation"].fillna(0.5)
# df.to_csv('temp23.csv')

for team in teams:
    df = df.drop(columns=[f"{team}_누적득점", f"{team}_누적실점"])
# df.to_csv('temp24.csv')
# print(df.columns)

# games back

### team 누적 승리, 패배 계산 ###
dic_win = {}
dic_lose = {}
for i in teams:
    dic_win[i] = 0
    dic_lose[i] = 0
for i, row in df.iterrows():
    home = row["home"]
    away = row["away"]
    home_score = row["home_score"]
    away_score = row["away_score"]
    if home_score > away_score:
        dic_win[home] += 1
        dic_lose[away] += 1
    elif away_score > home_score:
        dic_win[away] += 1
        dic_lose[home] += 1
    else:
        pass
    for team in teams:
        df.at[i, f"{team}_win"] = dic_win[team]
        df.at[i, f"{team}_lose"] = dic_lose[team]

# df.to_csv('temp25.csv')

# df['games_back'] = wjsdlf...
df.loc[0, "games_back"] = 0
for idx, row in df.iterrows():
    home = row["home"]
    away = row["away"]
    # if idx == 0:
    #     home_win = 0
    #     home_lose = 0
    #     away_win = 0
    #     away_lose = 0
    # else:
    #     home_win = df.loc[idx-1, f'{home}_win']
    #     away_win = df.loc[idx-1, f'{away}_lose']
    #     home_lose = df.loc[idx-1, f'{home}_lose']
    #     away_lose = df.loc[idx-1, f'{away}_lose']
    if idx != 0:
        df.loc[idx, "games_back"] = (
            abs(df.loc[idx - 1, f"{home}_win"] - df.loc[idx - 1, f"{away}_win"])
            + abs(df.loc[idx - 1, f"{home}_lose"] - df.loc[idx - 1, f"{away}_lose"])
        ) / 2

# df.to_csv('temp26.csv')

# home team 승률
df.loc[0, "home_win_rate"] = 0
for idx, row in df.iterrows():
    home = row["home"]
    if idx != 0:
        df.loc[idx, "home_win_rate"] = df.loc[idx - 1, f"{home}_win"] / (
            df.loc[idx - 1, f"{home}_win"] + df.loc[idx - 1, f"{home}_lose"]
        )

# df.to_csv('temp27.csv')

for team in teams:
    df = df.drop(columns=[f"{team}_win", f"{team}_lose"])


## 전 3경기 전적

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
dic = {"win": "lose", "lose": "win", "even": "even"}
temp_list = []
a = 0
for team in teams:
    teams.remove(team)
    for t in teams:
        fd_df = df[
            df["home"].isin([f"{team}", f"{t}"]) & df["away"].isin([f"{team}", f"{t}"])
        ]
        fd_df["index"] = fd_df.index
        fd_df.index = range(len(fd_df))

        for idx, row in fd_df.iterrows():
            temp = []
            if idx > 2:
                home_now = row["home"]
                home_last1 = fd_df.loc[idx - 1, "home"]
                home_last2 = fd_df.loc[idx - 2, "home"]
                home_last3 = fd_df.loc[idx - 3, "home"]
                if home_now == home_last1:
                    last1 = row["last_match"]
                else:
                    last1 = dic[row["last_match"]]
                if home_now == home_last2:
                    last2 = fd_df.loc[idx - 1, "last_match"]
                else:
                    last2 = dic[fd_df.loc[idx - 1, "last_match"]]
                if home_now == home_last3:
                    last3 = fd_df.loc[idx - 2, "last_match"]
                else:
                    last3 = dic[fd_df.loc[idx - 2, "last_match"]]
                temp.extend([last1, last2, last3])
                win_count = temp.count("win")
                lose_count = temp.count("lose")
                even_count = temp.count("even")
                fd_df.loc[idx, "3game_results"] = f"{win_count}, {lose_count}"
                fd_df.loc[idx, "3game_evens"] = str(even_count)
        fd_df.index = fd_df["index"]
        fd_df = fd_df.drop(columns="index")
        temp_list.append(fd_df)

for team in teams:
    teams.remove(team)
    for t in teams:
        fd_df = df[
            df["home"].isin([f"{team}", f"{t}"]) & df["away"].isin([f"{team}", f"{t}"])
        ]
        fd_df["index"] = fd_df.index
        fd_df.index = range(len(fd_df))

        for idx, row in fd_df.iterrows():
            temp = []
            if idx > 2:
                home_now = row["home"]
                home_last1 = fd_df.loc[idx - 1, "home"]
                home_last2 = fd_df.loc[idx - 2, "home"]
                home_last3 = fd_df.loc[idx - 3, "home"]
                if home_now == home_last1:
                    last1 = row["last_match"]
                else:
                    last1 = dic[row["last_match"]]
                if home_now == home_last2:
                    last2 = fd_df.loc[idx - 1, "last_match"]
                else:
                    last2 = dic[fd_df.loc[idx - 1, "last_match"]]
                if home_now == home_last3:
                    last3 = fd_df.loc[idx - 2, "last_match"]
                else:
                    last3 = dic[fd_df.loc[idx - 2, "last_match"]]
                temp.extend([last1, last2, last3])
                win_count = temp.count("win")
                lose_count = temp.count("lose")
                even_count = temp.count("even")
                fd_df.loc[idx, "3game_results"] = f"{win_count}, {lose_count}"
                fd_df.loc[idx, "3game_evens"] = str(even_count)
        fd_df.index = fd_df["index"]
        fd_df = fd_df.drop(columns="index")
        temp_list.append(fd_df)
# print(team, t)
fd_df = df[df["home"].isin([f"{team}", f"{t}"]) & df["away"].isin([f"{team}", f"{t}"])]
fd_df["index"] = fd_df.index
fd_df.index = range(len(fd_df))

for idx, row in fd_df.iterrows():
    temp = []
    if idx > 2:
        home_now = row["home"]
        home_last1 = fd_df.loc[idx - 1, "home"]
        home_last2 = fd_df.loc[idx - 2, "home"]
        home_last3 = fd_df.loc[idx - 3, "home"]
        if home_now == home_last1:
            last1 = row["last_match"]
        else:
            last1 = dic[row["last_match"]]
        if home_now == home_last2:
            last2 = fd_df.loc[idx - 1, "last_match"]
        else:
            last2 = dic[fd_df.loc[idx - 1, "last_match"]]
        if home_now == home_last3:
            last3 = fd_df.loc[idx - 2, "last_match"]
        else:
            last3 = dic[fd_df.loc[idx - 2, "last_match"]]
        temp.extend([last1, last2, last3])
        win_count = temp.count("win")
        lose_count = temp.count("lose")
        even_count = temp.count("even")
        fd_df.loc[idx, "3game_results"] = f"{win_count}, {lose_count}"
        fd_df.loc[idx, "3game_evens"] = str(even_count)
fd_df.index = fd_df["index"]
fd_df = fd_df.drop(columns="index")
temp_list.append(fd_df)

merged_df = pd.concat(temp_list)
merged_df.sort_index(inplace=True)

merged_df["3game_results"] = merged_df["3game_results"].fillna(str(0))
merged_df["3game_evens"] = merged_df["3game_evens"].fillna(str(0))
merged_df.to_csv("./data/temp2023_3.csv")
