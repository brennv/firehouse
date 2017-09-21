import requests


def get_parcel(lat, lon):
    """ Retrieve parcel data for a given coordinate. """
    url = ('http://gis.richmondgov.com/ArcGIS/rest/services/WebMercator/Parcels/MapServer/2/query'
           '?geometryType=esriGeometryPoint&spatialRel=esriSpatialRelIntersects&returnCountOnly=false'
           '&returnIdsOnly=false&returnGeometry=true&f=pjson')
    url += f'&geometry={lon}%2C{lat}'
    response = requests.get(url)
    # TODO add error handler
    return response.json()
