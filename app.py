from flask import Flask, jsonify
from firehouse.data import data

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


@app.route('/data/raw')
def raw():
    return jsonify(data)


if __name__ == '__main__':
    app.run()
