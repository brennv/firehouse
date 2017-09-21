from shapely.geometry import Point, shape
import geojson


with open('demo/Fire_Districts.geojson') as f:
    # Load multipolygon from
    # data.richmondgov.com/Community-Safety-and-Well-Being/Fire-Districts/f9rn-dwnd
    mp = geojson.load(f)

district_names = [s['properties']['name'] for s in mp['features']]


def get_district(lat, lon):
    """ Check if polygons in a multiploygon contain a point.
    Return the property name for the intersecting polygon. """
    point = Point(float(lon), float(lat))
    point_in_poly = [shape(s['geometry']).contains(point) for s in mp['features']]
    index = point_in_poly.index(True)
    return district_names[index]
