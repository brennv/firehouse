[![Python Versions](https://img.shields.io/badge/Python-3.6-blue.svg)](https://travis-ci.org/brennv/firehouse)
[![Build Status](https://travis-ci.org/brennv/firehouse.svg?branch=master)](https://travis-ci.org/brennv/firehouse)
[![codecov](https://codecov.io/gh/brennv/firehouse/branch/master/graph/badge.svg)](https://codecov.io/gh/brennv/firehouse)


# firehouse

Enriching data from firehouse response logs with:

- Weather data for the day the incident from [Weather Underground](https://www.wunderground.com/history/)
- Parcel data for the incident location from [local GIS servers](http://gis.richmondgov.com/ArcGIS/SDK/REST/index.html?catalog.html)
- Fire district for the location of the incident from [local open-data](https://data.richmondgov.com/)

Example map: [https://fire.vonapp.co](https://fire.vonapp.co)

Example enriched json: [https://fire.vonapp.co/data](https://fire.vonapp.co/data)

Demo maps: [https://fire.vonapp.co/demo](https://fire.vonapp.co/demo)

Demo enriched json: [https://fire.vonapp.co/demo](https://fire.vonapp.co/demo) plus `<id>/data`


## Usage

Clone the repo, install requirements and start the server:

```
pip install -r requirements.txt
python app.py
```

To demo more reports, add json files to the `demo/` folder and visit the `<host>/demo` endpoint.

To get the enriched demo json, curl or navigate to `<host>/demo/<id>/data`.

To get enriched json you can also POST json to the `/data` endpoint. In Python it would look like:

```
import requests
import json

with open(filepath) as f:
      data = json.load(f)
response = requests.post('https://fire.vonapp.co/data', json=json.dumps(data))
print(response.json())
```

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

## Roadmap

- Session management
- Mapping multiple reports
- Contextual sidebar with report list
- api/ endpoints with swagger
- Caching 
