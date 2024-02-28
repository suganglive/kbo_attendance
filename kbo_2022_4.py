import random
import re
import time

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

import kbo_2023_html

df = pd.read_csv("./data/temp2022_3.csv", index_col=0)
# print(df)

dic_gal = {
    "NC": "https://gall.dcinside.com/board/lists/?id=ncdinos&page=",
    "KIA": "https://gall.dcinside.com/board/lists/?id=tigers_new&page=",
    "SSG": "https://gall.dcinside.com/board/lists/?id=skwyverns_new1&page=",
    "KT": "https://gall.dcinside.com/board/lists/?id=ktwiz&page=",
    "LG": "https://gall.dcinside.com/board/lists/?id=lgtwins_new&page=",
    "Kiwoom": "https://gall.dcinside.com/board/lists/?id=sh_new&page=",
    "Hanhwa": "https://gall.dcinside.com/board/lists/?id=hanwhaeagles_new&page=",
    "Samsung": "https://gall.dcinside.com/board/lists/?id=samsunglions_new&page=",
    "Doosan": "https://gall.dcinside.com/board/lists/?id=doosanbears_new1&page=",
    "Lotte": "https://gall.dcinside.com/board/lists/?id=giants_new2&page=",
}

teams = list(dic_gal)
dic = {}
for team in teams:
    temp_df = pd.read_csv(f"./data/{team}.csv", index_col=0)
    # temp_df['reply'] = pd.to_numeric(temp_df['reply'])
    temp_df["reply"] = pd.to_numeric(temp_df["reply"], errors="coerce")
    # print(temp_df)
    dic[team] = temp_df.groupby("date").sum().reset_index()
    # df['view', 'recommend', 'reply'] = df['view', 'recommend', 'reply'].shift(1)
    dic[team][["view", "recommend", "reply"]] = dic[team][
        ["view", "recommend", "reply"]
    ].shift(1)
    dic[team].fillna(dic[team].mean(), inplace=True)
    # print(dic[team].isnull().sum())

    # print(team, dic[team])

for idx, row in df.iterrows():
    home = row["home"]
    away = row["away"]
    date = row["date"]
    df.loc[idx, "home_view"] = (
        dic[home].loc[dic[home]["date"] == date, "view"].values[0]
    )
    df.loc[idx, "home_recommend"] = (
        dic[home].loc[dic[home]["date"] == date, "recommend"].values[0]
    )
    df.loc[idx, "home_reply"] = (
        dic[home].loc[dic[home]["date"] == date, "reply"].values[0]
    )

    df.loc[idx, "away_view"] = (
        dic[away].loc[dic[away]["date"] == date, "view"].values[0]
    )
    df.loc[idx, "away_recommend"] = (
        dic[away].loc[dic[away]["date"] == date, "recommend"].values[0]
    )
    df.loc[idx, "away_reply"] = (
        dic[away].loc[dic[away]["date"] == date, "reply"].values[0]
    )

df.to_csv("./data/temp2022_4.csv")

# dic_gal = {'NC':'https://gall.dcinside.com/board/lists/?id=ncdinos&page=',
#            'KIA':'https://gall.dcinside.com/board/lists/?id=tigers_new&page=',
#            'SSG':'https://gall.dcinside.com/board/lists/?id=skwyverns_new1&page=',
#            'KT':'https://gall.dcinside.com/board/lists/?id=ktwiz&page=',
#            'LG':'https://gall.dcinside.com/board/lists/?id=lgtwins_new&page=',
#            'Kiwoom':'https://gall.dcinside.com/board/lists/?id=sh_new&page=',
#            'Hanhwa':'https://gall.dcinside.com/board/lists/?id=hanwhaeagles_new&page=',
#            'Samsung':'https://gall.dcinside.com/board/lists/?id=samsunglions_new&page=',
#            'Doosan':'https://gall.dcinside.com/board/lists/?id=doosanbears_new1&page=',
#            'Lotte':'https://gall.dcinside.com/board/lists/?id=giants_new2&page='}

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
# }
# teams = list(dic_gal)
# dic = {}

# for team in teams:
#     date_lst = []
#     view_lst = []
#     recommend_lst = []
#     reply_lst = []

#     pg_num = 2
#     game = 0
#     while game==0:
#         # for team in teams:
#         response = requests.get(dic_gal[team]+str(pg_num)+'&exception_mode=recommend', headers=headers)
# ...
#         # print(response.status_code)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             # print(soup)
#             # Find all <tbody> elements with class="ub-content us-post" inside <tr>
#             tr_elements = soup.select('tbody tr.ub-content.us-post')

#             for tr in tr_elements:
#                 # Process or print the data within each tr element
#                 temp1 = tr.select_one('td.gall_date')
#                 date = temp1.get('title', '')[:10]
#                 date = date[:4] + date[5:7] + date[8:10]
#                 date = int(date)
#                 view = tr.select_one('td.gall_count').text
#                 num = tr.select_one('td.gall_num').text
#                 num = int(num)
#                 if pg_num ==2:
#                     previous_num = num
#                     filt = num/previous_num
#                 else:
#                     filt = num/previous_num
#                     previous_num = num
#                 # filt = num/previous_num
#                 try:
#                     recommend = tr.select_one('td.gall_recommend').text
#                 except:
#                     recommend = None
#                 try:
#                     reply = tr.select_one('span.reply_num').text.strip('[,]')
#                 except:
#                     reply = None

#                 if date > 20231018:
#                     pass
#                     # print(f'{date} to recent')
#                 elif date <= 20231018 and date >= 20220401:
#                     # df[(df.date >= 20230401) & (df.date <= 20231018)]
#                     # print(f'''
#                     #         date : {date},
#                     #         view : {view},
#                     #         recommend : {recommend},
#                     #         reply : {reply}''')
#                     date_lst.append(date)
#                     view_lst.append(view)
#                     recommend_lst.append(recommend)
#                     reply_lst.append(reply)
#                 elif filt <= 0.95:
#                     pass
#                     print(f'{filt} not user post')
#                 else:
#                     game = 1
#                     break

#             time.sleep(random.uniform(0, 0.1))
#             print(team, pg_num, 'done')
#             previous_num = num
#             pg_num += 1
#     data = {'date': date_lst, 'view': view_lst, 'recommend': recommend_lst, 'reply': reply_lst}
#     df = pd.DataFrame(data)
#     dic[team] = df
#     dic[team].to_csv(f'{team}.csv')

# for team in teams:
#     dic[team].to_csv(f'{team}_save.csv')
