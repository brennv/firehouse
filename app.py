from flask import Flask, jsonify, render_template
from firehouse.data import enrich_data
from firehouse.map import create_map
from firehouse.weather import get_weather
from firehouse.parcel import get_parcel


app = Flask(__name__)
# demo_json = 'demo/F01705150050.json'
demo_json = 'demo/F01705150090.json'
data = enrich_data(demo_json)


@app.route('/')
@app.route('/map')
def show_map():
    _map = create_map(data)
    return render_template('map.html', map=_map)


@app.route('/data')
def show_data():
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
