expected_map = ('<div style="width:100%;"><div style="position:relative;width:100%;'
                'height:0;padding-bottom:60%;"><iframe src="data:text/html;'
                'charset=utf-8;base64,.." style="position:absolute;width:100%;'
                'height:100%;left:0;top:0;border:none !important;" '
                'allowfullscreen webkitallowfullscreen mozallowfullscreen>'
                '</iframe></div></div>')

expected_popup = """
        <h4>333 E FRANKLIN ST</h4>
        <h5>2017-05-15 13:19<h5>
        <code>HAZMAT: SMELL OR ODOR (NO SPILL)</code>
        <p>Weather: Partly Cloudy</p>
        <p>Parcel: 102100</p>
        <p>Stations involved: FSTA22</p>
        <p>Fire district: 6</p>
"""

expected_data = {
  "address": {
    "address_id": "",
    "address_line1": "333 E FRANKLIN ST",
    "city": "Richmond",
    "common_place_name": "MEDIA GENERAL - TIMES DISPATCH",
    "cross_street1": "N 3RD ST",
    "cross_street2": "N 4TH ST",
    "first_due": "6",
    "geohash": "dq8vtf33qdte",
    "latitude": 37.541885,
    "longitude": -77.440624,
    "name": "FRANKLIN",
    "number": "333",
    "postal_code": "",
    "prefix_direction": "E",
    "response_zone": "701601",
    "state": "VA",
    "suffix_direction": "",
    "type": "ST"
  },
  "apparatus": [
    {
      "car_id": "891284",
      "extended_data": {
        "event_duration": 4134,
        "response_duration": 762,
        "travel_duration": 504,
        "turnout_duration": 258
      },
      "geohash": "dq8vhztwn5ym",
      "personnel": [],
      "shift": "B",
      "station": "FSTA22",
      "unit_id": "H3",
      "unit_status": {
        "acknowledged": {
          "geohash": "dq8vhztwn5ym",
          "latitude": 37.483656,
          "longitude": -77.478753,
          "timestamp": "2017-05-15T13:21:38-04:00"
        },
        "arrived": {
          "geohash": "dq8vtf33qdte",
          "latitude": 37.541885,
          "longitude": -77.440624,
          "timestamp": "2017-05-15T13:32:12-04:00"
        },
        "available": {
          "geohash": "dq8vtf33qdte",
          "latitude": 37.541885,
          "longitude": -77.440624,
          "timestamp": "2017-05-15T14:28:24-04:00"
        },
        "cleared": {
          "geohash": "dq8vhztwn5ym",
          "latitude": 37.483656,
          "longitude": -77.478753,
          "timestamp": "2017-05-15T13:32:04-04:00"
        },
        "dispatched": {
          "geohash": "dq8vhztwn5ym",
          "latitude": 37.483656,
          "longitude": -77.478753,
          "timestamp": "2017-05-15T13:19:30-04:00"
        },
        "enroute": {
          "geohash": "dq8vhztwn5ym",
          "latitude": 37.483656,
          "longitude": -77.478753,
          "timestamp": "2017-05-15T13:23:48-04:00"
        },
        "~": {
          "geohash": "dq8vhztwn5ym",
          "latitude": 37.483656,
          "longitude": -77.478753,
          "timestamp": "2017-05-15T13:31:48-04:00"
        }
      },
      "unit_type": "Hazmat Unit"
    },
    {
      "car_id": "121310",
      "extended_data": {
        "event_duration": 4132,
        "response_duration": 762,
        "travel_duration": 713,
        "turnout_duration": 49
      },
      "geohash": "dq8vhztwm8pw",
      "personnel": [],
      "shift": "B",
      "station": "FSTA22",
      "unit_id": "T22",
      "unit_status": {
        "arrived": {
          "geohash": "dq8vtf27fxu9",
          "latitude": 37.542342,
          "longitude": -77.44217,
          "timestamp": "2017-05-15T13:32:12-04:00"
        },
        "available": {
          "geohash": "dq8vhzubkktu",
          "latitude": 37.484046,
          "longitude": -77.479859,
          "timestamp": "2017-05-15T14:28:22-04:00"
        },
        "cleared": {
          "geohash": "dq8vmqkemjqy",
          "latitude": 37.520271,
          "longitude": -77.458196,
          "timestamp": "2017-05-15T13:28:25-04:00"
        },
        "dispatched": {
          "geohash": "dq8vhztwm8pw",
          "latitude": 37.483679,
          "longitude": -77.478773,
          "timestamp": "2017-05-15T13:19:30-04:00"
        },
        "enroute": {
          "geohash": "dq8vhztwm8pw",
          "latitude": 37.483679,
          "longitude": -77.478773,
          "timestamp": "2017-05-15T13:20:19-04:00"
        },
        "~": {
          "geohash": "dq8vmq5rwvb8",
          "latitude": 37.519629,
          "longitude": -77.459846,
          "timestamp": "2017-05-15T13:28:19-04:00"
        }
      },
      "unit_type": "Truck/Aerial"
    },
    {
      "car_id": "161330",
      "extended_data": {
        "event_duration": 5234,
        "response_duration": 769,
        "travel_duration": 688,
        "turnout_duration": 81
      },
      "geohash": "dq8vhztwr80y",
      "personnel": [],
      "shift": "B",
      "station": "FSTA22",
      "unit_id": "E22",
      "unit_status": {
        "arrived": {
          "geohash": "dq8vmwb9qrb6",
          "latitude": 37.522687,
          "longitude": -77.452658,
          "timestamp": "2017-05-15T13:32:20-04:00"
        },
        "available": {
          "geohash": "dq8vhztwjff9",
          "latitude": 37.48365,
          "longitude": -77.478769,
          "timestamp": "2017-05-15T14:46:45-04:00"
        },
        "cleared": {
          "geohash": "dq8vmwb9qrb6",
          "latitude": 37.522687,
          "longitude": -77.452658,
          "timestamp": "2017-05-15T13:29:02-04:00"
        },
        "dispatched": {
          "geohash": "dq8vhztwr80y",
          "latitude": 37.483679,
          "longitude": -77.478696,
          "timestamp": "2017-05-15T13:19:31-04:00"
        },
        "enroute": {
          "geohash": "dq8vhztwr80y",
          "latitude": 37.483679,
          "longitude": -77.478696,
          "timestamp": "2017-05-15T13:20:52-04:00"
        },
        "~": {
          "geohash": "dq8vmwb9qrb6",
          "latitude": 37.522687,
          "longitude": -77.452658,
          "timestamp": "2017-05-15T13:28:52-04:00"
        }
      },
      "unit_type": "Engine"
    },
    {
      "car_id": "091299",
      "extended_data": {
        "event_duration": 4143,
        "response_duration": 761,
        "travel_duration": 508,
        "turnout_duration": 253
      },
      "geohash": "dq8vhztwn5ym",
      "personnel": [],
      "shift": "B",
      "station": "FSTA22",
      "unit_id": "H2",
      "unit_status": {
        "acknowledged": {
          "geohash": "dq8vhztwn5ym",
          "latitude": 37.483656,
          "longitude": -77.478753,
          "timestamp": "2017-05-15T13:21:36-04:00"
        },
        "arrived": {
          "geohash": "dq8vtf33qdte",
          "latitude": 37.541885,
          "longitude": -77.440624,
          "timestamp": "2017-05-15T13:32:12-04:00"
        },
        "available": {
          "geohash": "dq8vtf33qdte",
          "latitude": 37.541885,
          "longitude": -77.440624,
          "timestamp": "2017-05-15T14:28:34-04:00"
        },
        "cleared": {
          "geohash": "dq8vhztwn5ym",
          "latitude": 37.483656,
          "longitude": -77.478753,
          "timestamp": "2017-05-15T13:32:04-04:00"
        },
        "dispatched": {
          "geohash": "dq8vhztwn5ym",
          "latitude": 37.483656,
          "longitude": -77.478753,
          "timestamp": "2017-05-15T13:19:31-04:00"
        },
        "enroute": {
          "geohash": "dq8vhztwn5ym",
          "latitude": 37.483656,
          "longitude": -77.478753,
          "timestamp": "2017-05-15T13:23:44-04:00"
        },
        "~": {
          "geohash": "dq8vhztwn5ym",
          "latitude": 37.483656,
          "longitude": -77.478753,
          "timestamp": "2017-05-15T13:31:44-04:00"
        }
      },
      "unit_type": "Hazmat Unit"
    }
  ],
  "description": {
    "comments": "** LOI search completed at 05/15/17 13:19:12 SPECIAL ADDRESS COMMENT: ***RFD: TARGET HAZARD*** ** Case number C201713827 has been assigned to event F01705150050 ** >>>> by: NANCY L. MOREY on terminal: ecc-f1 OLD BOX OF CHEMICALS WANTS IT TO BE CHECKED OUT *****************TAC 3******************* T22/H2/H3 OS - LT FROM T22 HAS CMD",
    "day_of_week": "Monday",
    "event_closed": "2017-05-15T14:46:46-04:00",
    "event_id": "3587288",
    "event_opened": "2017-05-15T13:19:12-04:00",
    "extended_data": {
      "dispatch_duration": 18,
      "event_duration": 5254,
      "response_time": 762
    },
    "first_unit_arrived": "2017-05-15T13:32:12-04:00",
    "first_unit_dispatched": "2017-05-15T13:19:30-04:00",
    "first_unit_enroute": "2017-05-15T13:20:19-04:00",
    "hour_of_day": 13,
    "incident_number": "F01705150050",
    "loi_search_complete": "2017-05-15T13:19:12-04:00",
    "subtype": "SMELL OR ODOR (NO SPILL)",
    "type": "HAZMAT"
  },
  "district": "6",
  "fire_department": {
    "fd_id": "76000",
    "firecares_id": "93345",
    "name": "Richmond Fire and Emergency Services",
    "shift": "B",
    "state": "VA",
    "timezone": "US/Eastern"
  },
  "parcel": {
    "displayFieldName": "OwnerName",
    "features": [],
    "fieldAliases": {
      "OwnerName": "OwnerName"
    },
    "fields": [
      {
        "alias": "OwnerName",
        "length": 100,
        "name": "OwnerName",
        "type": "esriFieldTypeString"
      }
    ],
    "geometryType": "esriGeometryPolygon",
    "spatialReference": {
      "wkid": 102100
    }
  },
  "version": "1.0.29",
  "weather": [
    {
      "Conditions": "Mostly Cloudy",
      "Dew Point": "50.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "46%",
      "Precip": "",
      "Pressure": "29.79\u00a0in",
      "Temp.": "71.6\u00a0\u00b0F",
      "Time (EDT)": "12:51 AM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "North",
      "Wind Speed": "12.7\u00a0mph"
    },
    {
      "Conditions": "Mostly Cloudy",
      "Dew Point": "50.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "49%",
      "Precip": "",
      "Pressure": "29.81\u00a0in",
      "Temp.": "70.0\u00a0\u00b0F",
      "Time (EDT)": "12:54 AM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "North",
      "Wind Speed": "13.8\u00a0mph"
    },
    {
      "Conditions": "Mostly Cloudy",
      "Dew Point": "48.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "52%",
      "Precip": "",
      "Pressure": "29.82\u00a0in",
      "Temp.": "66.0\u00a0\u00b0F",
      "Time (EDT)": "1:54 AM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "NNE",
      "Wind Speed": "13.8\u00a0mph"
    },
    {
      "Conditions": "Mostly Cloudy",
      "Dew Point": "45.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "50%",
      "Precip": "",
      "Pressure": "29.85\u00a0in",
      "Temp.": "64.0\u00a0\u00b0F",
      "Time (EDT)": "2:54 AM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "NNE",
      "Wind Speed": "11.5\u00a0mph"
    },
    {
      "Conditions": "Mostly Cloudy",
      "Dew Point": "35.1\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "35%",
      "Precip": "",
      "Pressure": "29.88\u00a0in",
      "Temp.": "63.0\u00a0\u00b0F",
      "Time (EDT)": "3:54 AM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "North",
      "Wind Speed": "10.4\u00a0mph"
    },
    {
      "Conditions": "Mostly Cloudy",
      "Dew Point": "32.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "32%",
      "Precip": "",
      "Pressure": "29.89\u00a0in",
      "Temp.": "62.1\u00a0\u00b0F",
      "Time (EDT)": "4:54 AM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "North",
      "Wind Speed": "12.7\u00a0mph"
    },
    {
      "Conditions": "Mostly Cloudy",
      "Dew Point": "33.1\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "36%",
      "Precip": "",
      "Pressure": "29.91\u00a0in",
      "Temp.": "60.1\u00a0\u00b0F",
      "Time (EDT)": "5:54 AM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "North",
      "Wind Speed": "5.8\u00a0mph"
    },
    {
      "Conditions": "Scattered Clouds",
      "Dew Point": "36.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "42%",
      "Precip": "",
      "Pressure": "29.94\u00a0in",
      "Temp.": "59.0\u00a0\u00b0F",
      "Time (EDT)": "6:54 AM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "North",
      "Wind Speed": "6.9\u00a0mph"
    },
    {
      "Conditions": "Scattered Clouds",
      "Dew Point": "36.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "41%",
      "Precip": "",
      "Pressure": "29.96\u00a0in",
      "Temp.": "60.1\u00a0\u00b0F",
      "Time (EDT)": "7:54 AM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "North",
      "Wind Speed": "10.4\u00a0mph"
    },
    {
      "Conditions": "Partly Cloudy",
      "Dew Point": "37.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "38%",
      "Precip": "",
      "Pressure": "29.97\u00a0in",
      "Temp.": "63.0\u00a0\u00b0F",
      "Time (EDT)": "8:54 AM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "North",
      "Wind Speed": "10.4\u00a0mph"
    },
    {
      "Conditions": "Partly Cloudy",
      "Dew Point": "37.9\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "19.6\u00a0mph",
      "Humidity": "36%",
      "Precip": "",
      "Pressure": "29.97\u00a0in",
      "Temp.": "66.0\u00a0\u00b0F",
      "Time (EDT)": "9:54 AM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "NNW",
      "Wind Speed": "13.8\u00a0mph"
    },
    {
      "Conditions": "Partly Cloudy",
      "Dew Point": "36.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "30%",
      "Precip": "",
      "Pressure": "29.97\u00a0in",
      "Temp.": "69.1\u00a0\u00b0F",
      "Time (EDT)": "10:54 AM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "NW",
      "Wind Speed": "15.0\u00a0mph"
    },
    {
      "Conditions": "Partly Cloudy",
      "Dew Point": "37.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "23.0\u00a0mph",
      "Humidity": "29%",
      "Precip": "",
      "Pressure": "29.96\u00a0in",
      "Temp.": "71.1\u00a0\u00b0F",
      "Time (EDT)": "11:54 AM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "North",
      "Wind Speed": "17.3\u00a0mph"
    },
    {
      "Conditions": "Partly Cloudy",
      "Dew Point": "37.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "26%",
      "Precip": "",
      "Pressure": "29.94\u00a0in",
      "Temp.": "73.9\u00a0\u00b0F",
      "Time (EDT)": "12:54 PM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "NNW",
      "Wind Speed": "17.3\u00a0mph"
    },
    {
      "Conditions": "Partly Cloudy",
      "Dew Point": "36.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "21.9\u00a0mph",
      "Humidity": "24%",
      "Precip": "",
      "Pressure": "29.94\u00a0in",
      "Temp.": "75.0\u00a0\u00b0F",
      "Time (EDT)": "1:54 PM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "NW",
      "Wind Speed": "12.7\u00a0mph"
    },
    {
      "Conditions": "Partly Cloudy",
      "Dew Point": "34.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "21%",
      "Precip": "",
      "Pressure": "29.92\u00a0in",
      "Temp.": "77.0\u00a0\u00b0F",
      "Time (EDT)": "2:54 PM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "NW",
      "Wind Speed": "11.5\u00a0mph"
    },
    {
      "Conditions": "Partly Cloudy",
      "Dew Point": "37.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "22%",
      "Precip": "",
      "Pressure": "29.91\u00a0in",
      "Temp.": "79.0\u00a0\u00b0F",
      "Time (EDT)": "3:54 PM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "NW",
      "Wind Speed": "13.8\u00a0mph"
    },
    {
      "Conditions": "Clear",
      "Dew Point": "37.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "21%",
      "Precip": "",
      "Pressure": "29.89\u00a0in",
      "Temp.": "80.1\u00a0\u00b0F",
      "Time (EDT)": "4:54 PM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "NNW",
      "Wind Speed": "12.7\u00a0mph"
    },
    {
      "Conditions": "Clear",
      "Dew Point": "36.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "21%",
      "Precip": "",
      "Pressure": "29.90\u00a0in",
      "Temp.": "79.0\u00a0\u00b0F",
      "Time (EDT)": "5:54 PM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "NNW",
      "Wind Speed": "8.1\u00a0mph"
    },
    {
      "Conditions": "Clear",
      "Dew Point": "39.9\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "26%",
      "Precip": "",
      "Pressure": "29.91\u00a0in",
      "Temp.": "77.0\u00a0\u00b0F",
      "Time (EDT)": "6:54 PM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "North",
      "Wind Speed": "6.9\u00a0mph"
    },
    {
      "Conditions": "Partly Cloudy",
      "Dew Point": "43.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "35%",
      "Precip": "",
      "Pressure": "29.94\u00a0in",
      "Temp.": "72.0\u00a0\u00b0F",
      "Time (EDT)": "7:54 PM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "North",
      "Wind Speed": "5.8\u00a0mph"
    },
    {
      "Conditions": "Partly Cloudy",
      "Dew Point": "46.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "48%",
      "Precip": "",
      "Pressure": "29.96\u00a0in",
      "Temp.": "66.0\u00a0\u00b0F",
      "Time (EDT)": "8:54 PM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "NE",
      "Wind Speed": "3.5\u00a0mph"
    },
    {
      "Conditions": "Partly Cloudy",
      "Dew Point": "46.9\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "56%",
      "Precip": "",
      "Pressure": "29.99\u00a0in",
      "Temp.": "63.0\u00a0\u00b0F",
      "Time (EDT)": "9:54 PM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "Calm",
      "Wind Speed": "Calm"
    },
    {
      "Conditions": "Clear",
      "Dew Point": "48.9\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "74%",
      "Precip": "",
      "Pressure": "30.02\u00a0in",
      "Temp.": "57.0\u00a0\u00b0F",
      "Time (EDT)": "10:54 PM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "Calm",
      "Wind Speed": "Calm"
    },
    {
      "Conditions": "Clear",
      "Dew Point": "46.0\u00a0\u00b0F",
      "Events": "",
      "Gust Speed": "-",
      "Humidity": "67%",
      "Precip": "",
      "Pressure": "30.04\u00a0in",
      "Temp.": "57.0\u00a0\u00b0F",
      "Time (EDT)": "11:54 PM",
      "Visibility": "10.0\u00a0mi",
      "Wind Dir": "Calm",
      "Wind Speed": "Calm"
    }
  ]
}
