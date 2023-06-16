import requests

url = "https://hue1.id.seabank.io/hue/accounts/login"
headers = {
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
           "Accept-Encoding":"gzip, deflate, br",
           "Accept-Language":"en-US,en;q=0.9",
           "Cache-Control":"max-age=0",
           "Content-Length":"134",
           "Content-Type":"application/x-www-form-urlencoded",
           "Cookie":"_ga=GA1.2.1710490959.1685329622; _gid=GA1.2.1020773365.1686716511; csrftoken=jIsKD2BEyfz3zxEvHEtA4RsubYRoPIZl1QQ8zQgGzlsNfAYpFTmfbLBNZP7oEVMg; sessionid=jq8p8q1f2zsk2ohsc9kzn78hajikwoqn; _gat=1",
           "Origin":"https://hue1.id.seabank.io",
           "Referer":"https://hue1.id.seabank.io/hue/accounts/login?next=/",
           "Sec-Ch-Ua-Mobile":"0","Sec-Ch-Ua-Platform":"Windows","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",}


body = {"csrfmiddlewaretoken": "nbhavIR1Lb7Xw5WyETVu9yMcgYjd56ZMg7MohKLzXMmKlTMymhtu3XNw42tqMFUM","username": "muhammad.huda","password": "UPj8sksr","next": "/"}

login = requests.post(url, data=body, headers=headers)


from dataclasses import dataclass
from typing import Protocol
import psycopg2

@dataclass
class Connection:
    host: str = "localhost"
    port: int
    username: str
    password: str
    database: str

class ConnectionInterface(Protocol):
    """Interface connection for database connection"""
    def connect():
        """CTA for connect to database as choosen"""

    def save():
        """CTA to save connection in db.ini"""

class ImpalaConnection(ConnectionInterface):
    def connect(self):
        self.connection = Connection()

    def save(self):
        with open("db.ini", "w") as f:
            f.write(self.connection) 

class PostgreSQL(ConnectionInterface):
    def connect():
        pass

    def save():
        pass

    def log():
        pass