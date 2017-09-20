import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_weather(zipcode, year, month, day, hour=None):
    """ Retrieve hourly weather data for a specified date.
    If given an hour, only return data for that hour. """
    url = (f'https://www.wunderground.com/history/airport/KRIC/{year}/{month}/{day}'
           f'/DailyHistory.html?reqdb.zip={zipcode}&reqdb.magic=1&reqdb.wmo=99999&MR=1')
    response = requests.get(url)
    # TODO add error handler
    soup = BeautifulSoup(response.text, 'html5lib')
    table = soup.find_all('table')[-1]
    df = pd.read_html(str(table))[0]
    df = df.fillna('')
    weather = df.to_dict(orient='records')
    if hour != None:
        weather = weather[hour]
    return weather
