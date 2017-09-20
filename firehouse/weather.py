import requests
import pandas as pd
from bs4 import BeautifulSoup
import html5lib
from io import StringIO


year, month, day = 2013, 9, 20
url = f'https://www.wunderground.com/history/airport/KRIC/{year}/{month}/{day}/DailyHistory.html?req_city=Richmond&req_state=VA&req_statename=Virginia&reqdb.zip=23218&reqdb.magic=1&reqdb.wmo=99999&MR=1'
print(url)

response = requests.get(url)
print(response)

soup = BeautifulSoup(response.text, 'html5lib')
table = soup.find_all('table')[-1]

with open('env/temp.txt') as f:
    f.write(table)

df = pd.read_html(StringIO(table))

print(df)
