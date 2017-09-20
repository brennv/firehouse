from flask import Flask, jsonify, render_template
from firehouse.data import data
from firehouse.map import create_map
from firehouse.weather import get_weather

app = Flask(__name__)



@app.route('/data')
def data():
    return jsonify(data)


@app.route('/')
@app.route('/map')
def map():
    _map = create_map(data)
    return render_template('map.html', map=_map)


@app.route('/weather/<zipcode>/<year>/<month>/<day>')
def weather():
    hourly_weather = get_weather(zipcode, year, month, day)
    return jsonify(hourly_weather)


if __name__ == '__main__':
    app.run(debug=True)
