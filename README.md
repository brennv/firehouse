[![Python Versions](https://img.shields.io/badge/Python-3.6-blue.svg)](https://travis-ci.org/brennv/firehouse)
[![Build Status](https://travis-ci.org/brennv/firehouse.svg?branch=master)](https://travis-ci.org/brennv/firehouse)
[![codecov](https://codecov.io/gh/brennv/firehouse/branch/master/graph/badge.svg)](https://codecov.io/gh/brennv/firehouse)


# firehouse

Enriching data from firehouse response logs with:

- Weather data for the day the incident from [Weather Underground](https://www.wunderground.com/history/)
- Parcel data for the incident location from [local GIS servers](http://gis.richmondgov.com/ArcGIS/SDK/REST/index.html?catalog.html)
- Fire district for the location of the incident from [local open-data](https://data.richmondgov.com/)

Default map: [https://fire.vonapp.co](https://fire.vonapp.co)

All demo maps: [https://fire.vonapp.co](https://fire.vonapp.co/demo)

Enriched json data: [https://fire.vonapp.co/data](https://fire.vonapp.co/data)

## Usage

Clone the repo, install requirements and start the server:

```
pip install -r requirements.txt
python app.py
```

To demo more reports, add json files to the `demo/` folder and visit the `<host>/demo` endpoint.

To get enriched json you can POST json to the `/data` endpoint. In Python it would look like:

```
import requests
import json

with open(filepath) as f:
      data = json.load(f)
response = requests.post('https://fire.vonapp.co/data', json=json.dumps(data))
print(response.json())
```

Alternatively, you can change the filepath for demo json in `app.py`.

## Development

Install package and dev requirements:

```
pip install -r requirements.txt
pip install pytest pytest-cov pylama
```

Tests and linting run with:

```
pytest -v --cov=firehouse/ tests/ && pylama -i E501 firehouse/
```
