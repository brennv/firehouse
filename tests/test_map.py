from tests.demo import expected_data, expected_map, expected_popup
from firehouse.map import create_map, create_popup


def test_excepted_demo_map_popup():
     assert create_popup(expected_data).strip() == expected_popup.strip()


def test_expected_demo_map():
    # TODO sort out base64 assertions
    # assert create_map(expected_data).strip() == expected_map.strip()
    pass
