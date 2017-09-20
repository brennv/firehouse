from .weather import get_weather
import json

with open('demo/data/F01705150050.json') as f:
    data = json.load(f)

event_opened = data['description']['event_opened']
date, time = event_opened.split('T')
year, month, day = date.split('-')
hour = time.split(':')[0]
zipcode = '23218'  # TODO geocode address
data['weather'] = get_weather(zipcode, year, month, day)
