from tests.demo import expected_data
from firehouse.data import enrich_data
import requests
import json


filepath = 'demo/F01705150050.json'


def test_expected_demo_data():
    assert enrich_data(filepath) == expected_data


def test_expected_post_data():
    # with open(filepath) as f:
    #     data = json.load(f)
    # response = requests.post('http://127.0.0.1:5000/data', json=json.dumps(data))  # TODO add host configs
    # assert response.json() == expected_data
    pass


# curl -vX POST http://127.0.0.1:5000/data -d demo/F01705150050.json --header "Content-Type: application/json"
