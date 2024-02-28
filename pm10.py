import pandas as pd

df = pd.read_csv("./data/pm10.csv")
df.columns = ["point", "where", "date", "figure"]
pivoted_df = df.pivot(index="date", columns="where", values="figure")
pivoted_df["avg"] = pivoted_df[["광주", "구덕산", "대구", "서울", "수원", "천안"]].mean(
    axis=1
)
pivoted_df = pivoted_df.T.fillna(pivoted_df["avg"]).T
df = pivoted_df
df = df.drop(columns="avg")
df["date"] = df.index


def datemodify(dff):
    lst = []
    for i in dff["date"]:
        i = i.split("/")
        i = "".join(i)
        lst.append(i)
    dff["date"] = lst
    return dff


df = datemodify(df)
# print(df)
