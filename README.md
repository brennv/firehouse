# firehouse

Enriching data from firehouse response logs with:

- weather data for the day the incident
- local GIS parcel data for the incident location

Demo map: [https://fire.vonapp.co](https://fire.vonapp.co)

Demo data: [https://fire.vonapp.co/data](https://fire.vonapp.co/data)

## Usage

Clone the repo, install requirements and start the server:

```python
pip install -r requirements.txt
python app.py
```

## Development

Install package and dev requirements:

```python
pip install -r requirements.txt
pip install pytest pytest-cov pylama
```

Tests and linting run with:

```python
pytest -v --cov=firehouse/ tests/ && pylama -i E501 firehouse/
```
