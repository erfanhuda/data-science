import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date, datetime
import schedule
import time

## Created by Muhammad Erfan Huda
## Follow on GitHub : @mandauhitam

today = date.today()
tm = str(datetime.time(datetime.now()))

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

def gold_silver():
    URL = 'https://www.logammulia.com/id'
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    base = soup.find("div", class_="hero-price")
    rows = [i.text for i in base.find_all("div", class_="ngc-title")]
    columns = [i.text.replace('\n', '').replace('\t','').replace("Harga/gram Rp", '') for i in base.find_all("span", class_="current")]

    df = pd.DataFrame(columns=rows)
    for i in range(1, len(rows)):
        df = df.append(pd.Series(columns, index=rows), ignore_index=True)
        print(df, str(datetime.now()))

schedule.every().day.at("20:59").do(gold_silver)

while True:
    schedule.run_pending()
    time.sleep(1)