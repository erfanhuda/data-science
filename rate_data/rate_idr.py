import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import schedule
import time

## Created by Erfan
## Follow on GitHub : @mandauhitam

class RateBot():
    def __init__(self, clock):
        self.today = date.today()
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
        self.URL_BI = 'https://www.bi.go.id/id/moneter/informasi-kurs/transaksi-bi/Default.aspx'
        self.URL_Pajak = 'https://www.ortax.org/ortax/?mod=kurs'
        self.clock = clock

    def rate_bi(self):
        page = requests.get(self.URL_BI, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        tdate = soup.find_all(id="ctl00_PlaceHolderMain_biWebKursTransaksiBI_lblUpdate")
        fdate = tdate[0].text

        table = soup.find("table", class_="table1")
        rows = table.find_all('tr')
        columns = [i.text.replace('Grafik', '') for i in rows[0].find_all('th')]

        df = pd.DataFrame(columns=columns)
        for i in range(1, len(rows)):
            tds = rows[i].find_all('td')
            if len(tds) == 4:
                values = [tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text.replace('\n\n', '')]
            else:
                values = [td.text.replace('\n', '').replace('\xa0', '') for td in tds]
            df = df.append(pd.Series(values, index=columns), ignore_index=True)
            print(df, fdate)

            df.to_excel(str(self.today)+' rate_bi.xlsx', index=False)

    def rate_pajak(self):
        page = requests.get(self.URL_Pajak, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        base = soup.find("div", class_="bs-docs-example")
        fdate = base.find_all("b")[0]

        table = base.find("table", id ="table")
        rows = table.find_all('tr')
        columns = [i.text.replace('Nilai', 'Rate') for i in rows[0].find_all('td')]

        df = pd.DataFrame(columns=columns)
        for i in range(1, len(rows)):
            tds = rows[i].find_all('td')
            if len(tds) == 4:
                values = [tds[1].text, tds[2].text, tds[3].text]
            else:
                values =[td.text.replace('\n', '').replace('\xa0', '') for td in tds]

            df = df.append(pd.Series(values, index=columns), ignore_index=True)
            print(df, fdate.text.replace('\n\t\t\t\t\t\t', ''))

            df.to_excel(fdate.text.replace('\n\t\t\t\t\t\t', '')+'rate_pajak.xlsx', index=False)

    def schedule(self):
        schedule.every().day.at(self.clock)
        while True:
            schedule.run_pending()
            time.sleep(1)
            schedule.clear()

runbot = RateBot('20:24')
runbot.rate_bi()
runbot.rate_pajak()
runbot.schedule()