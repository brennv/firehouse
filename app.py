from flask import Flask, jsonify, render_template, request
from firehouse.data import enrich_data
from firehouse.map import create_map
from firehouse.weather import get_weather
from firehouse.parcel import get_parcel
import json


app = Flask(__name__)
# demo_json = 'demo/F01705150050.json'
demo_json = 'demo/F01705150090.json'
demo_data = enrich_data(demo_json)


@app.route('/', methods=['GET', 'POST'])
@app.route('/map', methods=['GET', 'POST'])
def show_map():
    if request.method == 'POST':
        data = json.loads(request.get_json())
        data = enrich_data(filepath=None, data=data)
    else:
        data = demo_data
    _map = create_map(data)
    return render_template('map.html', map=_map)


@app.route('/data', methods=['GET', 'POST'])
def show_data():
    if request.method == 'POST':
        data = json.loads(request.get_json())
        data = enrich_data(filepath=None, data=data)
    else:
        data = demo_data
    return jsonify(data)


@app.route('/weather/<zipcode>/<year>/<month>/<day>')
def show_weather(zipcode, year, month, day):
    hourly_weather = get_weather(zipcode, year, month, day)
    return jsonify(hourly_weather)


@app.route('/parcel/<lat>/<lon>')
def show_parcel(lat, lon):
    parcel_data = get_parcel(lat, lon)
    return jsonify(parcel_data)


if __name__ == '__main__':
    app.run(debug=True)
