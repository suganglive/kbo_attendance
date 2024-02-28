import pandas as pd

# 구로구 20220401~20231108 일별 평균 기온, 일 강수량 자료 불러오기
df = pd.read_csv("./data/weather.csv")
pivoted_df = df.pivot(index="date", columns="where", values=["avg_temp", "rain"])

temp_df = pivoted_df["avg_temp"]
rain_df = pivoted_df["rain"]
temp_df["avg"] = temp_df[
    ["경산", "광명", "동래", "마산회원", "송파", "오월드", "의왕", "인천연수", "풍암"]
].mean(axis=1)
rain_df["avg"] = rain_df[
    ["경산", "광명", "동래", "마산회원", "송파", "오월드", "의왕", "인천연수", "풍암"]
].mean(axis=1)

temp_df = temp_df.T.fillna(temp_df["avg"]).T
rain_df = rain_df.T.fillna(rain_df["avg"]).T

temp_df["date"] = temp_df.index
rain_df["date"] = rain_df.index


def datemodify(dff):
    lst = []
    for i in dff["date"]:
        i = i.split("/")
        i = "".join(i)
        lst.append(i)
    dff["date"] = lst
    return dff


temp_df = datemodify(temp_df)
rain_df = datemodify(rain_df)

temp_df = temp_df.set_index(temp_df["date"])
rain_df = rain_df.set_index(temp_df["date"])
temp_df = temp_df.drop(columns="date")
rain_df = rain_df.drop(columns="date")

# print("temp", temp_df)
# print("rain", rain_df)
