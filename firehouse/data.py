from .weather import get_weather
from .parcel import get_parcel
import json


def enrich_data(filepath, data=None):
    """ Load json and enrich data with weather and parcel info. """
    if not filepath:
        data = data
    else:
        with open(filepath) as f:
            data = json.load(f)
    # TODO inspect data structure
    # Add weather data
    event_opened = data['description']['event_opened']
    date, time = event_opened.split('T')
    year, month, day = date.split('-')
    hour = int(time.split(':')[0])
    zipcode = '23218'  # TODO geocode address zipcodes
    data['weather'] = get_weather(zipcode, year, month, day)
    # Add parcel data
    lat, lon = data['address']['latitude'], data['address']['longitude']
    data['parcel'] = get_parcel(lat, lon)
    return data
