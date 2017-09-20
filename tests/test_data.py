from tests.demo import expected_data
from firehouse.data import data


def test_expected_data():
    assert data == expected_data
