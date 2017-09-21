from shapely.geometry import Point, shape
import geojson


with open('demo/Fire_Districts.geojson') as f:
    # Load multipolygon from
    # data.richmondgov.com/Community-Safety-and-Well-Being/Fire-Districts/f9rn-dwnd
    mp = geojson.load(f)


def find_district(lat, lon):
    point = Point(lon, lat)
    point_in_poly = [shape(s['geometry']).contains(point) for s in mp['features']]
    return point_in_poly.index(True)
