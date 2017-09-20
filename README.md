[![Python Versions](https://img.shields.io/badge/Python-3.6-blue.svg)](https://travis-ci.org/brennv/firehouse)
[![Build Status](https://travis-ci.org/brennv/firehouse.svg?branch=master)](https://travis-ci.org/brennv/firehouse)  

# firehouse

Enriching data from firehouse response logs with:

- weather data for the day the incident
- local GIS parcel data for the incident location

Demo map: [https://fire.vonapp.co](https://fire.vonapp.co)

Demo data: [https://fire.vonapp.co/data](https://fire.vonapp.co/data)

## Usage

Clone the repo, install requirements and start the server:

```
pip install -r requirements.txt
python app.py
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
