import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import schedule
import time

## Created by Muhammad Erfan Huda ##
## During COVID-19 ##

class StockBot:
    def __init__(self, stock):
        self.headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
        self.URL = 'http://www.duniainvestasi.com/bei/summaries/'
        self.stock = stock
        URL = self.URL + str(self.stock)
        page = requests.get(URL, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup)

    def stock_bot(self):
        URL = self.URL + str(self.stock)
        page = requests.get(URL, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup)

Stock = StockBot('ANTM')
Stock.stock_bot()