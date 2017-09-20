import folium
import optparse

richmond_coords = [37.53, -77.46]


def create_map():
    m = folium.Map(location=richmond_coords)
    filepath = os.path.join(os.getcwd(), 'templates/map.html')
    m.save(filepath)
    with open(filepath) as f:
        html = f.read()
    return html
