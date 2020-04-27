import requests
from bs4 import BeautifulSoup
from datetime import date, datetime

today = date.today()
time = datetime.time(datetime.now())

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

def gold_price():
    URL = 'https://id.investing.com/commodities/gold'
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id = "quotes_summary_current_data").find_all(dir="ltr")[0].text
    return price

while True:
    print("Date/Time :", time)
    print("Current Gold Price :" +str(gold_price()))