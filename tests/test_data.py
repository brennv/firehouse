from tests.demo import expected_data
from firehouse.data import enrich_data


def test_expected_data():
    assert enrich_data('demo/F01705150050.json') == expected_data
