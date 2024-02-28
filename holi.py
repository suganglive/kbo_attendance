import json
import os

import pandas as pd
import requests
from dotenv import load_dotenv
from pandas import json_normalize

# Load the environment variables from the .env file
load_dotenv()

# Access the API_KEY
HOLI_API_KEY = os.getenv("HOLI_API_KEY")


def get_holi(key, year):

    # openapi 활용 데이터 불러오기
    key = key
    url = (
        "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo?_type=json&numOfRows=50&solYear="
        + str(year)
        + "&ServiceKey="
        + str(key)
    )
    response = requests.get(url)
    if response.status_code == 200:
        json_ob = json.loads(response.text)
        holidays_data = json_ob["response"]["body"]["items"]["item"]
        dataframe = json_normalize(holidays_data)
        dataframe.loc[dataframe["locdate"] == int(year), "dateName"]
    return dataframe


dataframe2022 = get_holi(HOLI_API_KEY, 2022)
dataframe2023 = get_holi(HOLI_API_KEY, 2023)

# 2022, 2023 관중 데이터 병합
dfholi = pd.concat([dataframe2022, dataframe2023])
# print(dfholi)
