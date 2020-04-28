import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date, datetime

today = date.today()
time = datetime.time(datetime.now())

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

def gold_price():
    URL = 'https://www.logammulia.com/id'
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    base = soup.find("div", class_="hero-price")
    rows = base.find_all(class_="ngc-title")[0:2]
    columns = [i.text.replace('\n', '').replace('\t','').replace("Harga Terakhir: Rp", '') for i in base.find_all("p")]

    # print(columns)
    df = pd.DataFrame(columns=columns)
    # print(columns)
    for i in range(1, len(rows)):
        tds = columns[2:5]
        if len(tds) == 4:
            values = [tds[2].text, tds[4].text]
        else:
            values = [td.replace(".", "").replace(",", ".").replace("Harga/gram Rp8350.00Rp000", '') for td in tds]
        # print(values)
        df = df.appendll(pd.Series(values, index=rows), ignore_index=True)
        print(df)

    # emas = soup.find_all("p", class_="last-price")[0].text.strip()
    # perak = soup.find_all("p", class_="last-price")[1].text.strip()
    #

    # converted_emas = emas[18:].replace(".","").replace(",",".")
    # converted_perak = perak[18:].replace(".", "").replace(",", ".")
    # print(float(converted_emas), float(converted_perak))
    # converted_emas = float(price[0:5])
    # print(converted_emas)
gold_price()

# while True:
#     print("Date/Time :", time)
#     print("Current Gold Price :" +str(gold_price()))