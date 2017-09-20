from flask import Flask, jsonify, render_template
from firehouse.data import data
from firehouse.map import create_map

app = Flask(__name__)



@app.route('/data/raw')
def raw():
    return jsonify(data)


@app.route('/')
@app.route('/map')
def map():
    html = create_map()
    return render_template('map.html', map=html)


if __name__ == '__main__':
    app.run(debug=True)
