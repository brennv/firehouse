from firehouse import (enrich_data, create_map, get_weather, get_parcel,
                       get_district)
from flask import Flask, jsonify, render_template, request
import json
from os import listdir
from os.path import isfile, join


app = Flask(__name__)
demo_json = 'demo/F01705150050.json'
# demo_json = 'demo/F01705150090.json'
demo_data = enrich_data(demo_json)


@app.route('/', methods=['GET', 'POST'])
def show_map():
    """ Display the response data on a map. """
    if request.method == 'POST':
        # TODO add form to post data
        data = json.loads(request.get_json())
        data = enrich_data(filepath=None, data=data)
    else:
        data = demo_data
    _map = create_map(data)
    return render_template('map.html', map=_map)


@app.route('/demo')
@app.route('/demo/')
@app.route('/demo/<json_file_id>')
def show_jsonfile(json_file_id=''):
    """ For demo purposes, an endpoint for loading json files
    dynamically from the demo folder. """
    try:
        with open('demo/' + json_file_id + '.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = None
        files = [f for f in listdir('demo/') if isfile(join('demo/', f))]
        file_ids = [x.replace('.json', '') for x in files]
        urls = [f"<br><a href='/demo/{x}')>{x}</a>" for x in file_ids]
        _map = '<h3>Reports:</h3>' + ''.join(urls)
    if data is not None:
        data = enrich_data(filepath=None, data=data)
        _map = create_map(data)
    return render_template('map.html', map=_map)


@app.route('/data', methods=['GET', 'POST'])
def show_data():
    """ Enrich response data. """
    if request.method == 'POST':
        data = json.loads(request.get_json())
        data = enrich_data(filepath=None, data=data)
    else:
        data = demo_data
    return jsonify(data)


@app.route('/weather/<zipcode>/<year>/<month>/<day>')
def show_weather(zipcode, year, month, day):
    """ Retrieve weather data. """
    # TODO use paramaters instead of url path
    hourly_weather = get_weather(zipcode, year, month, day)
    return jsonify(hourly_weather)


@app.route('/parcel/<lat>/<lon>')
def show_parcel(lat, lon):
    """ Retrieve parcel data. """
    parcel_data = get_parcel(lat, lon)
    return jsonify(parcel_data)


@app.route('/district/<lat>/<lon>')
def show_district(lat, lon):
    """ Retrieve district data. """
    district = get_district(lat, lon)
    return jsonify({'district': district})


if __name__ == '__main__':
    # TODO add host configs, set threaded
    app.run(debug=True)  # intentionally left in debug mode for testing
