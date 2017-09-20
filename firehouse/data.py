from .weather import get_weather
from .parcel import get_parcel
import json

with open('demo/data/F01705150050.json') as f:
    data = json.load(f)

# Enrich data with weather data 
event_opened = data['description']['event_opened']
date, time = event_opened.split('T')
year, month, day = date.split('-')
hour = time.split(':')[0]
zipcode = '23218'  # TODO geocode address
data['weather'] = get_weather(zipcode, year, month, day)

# Enrich data with parcel data
lat, lon = data['address']['latitude'], data['address']['longitude']
data['parcel'] = get_parcel(lat, lon)
