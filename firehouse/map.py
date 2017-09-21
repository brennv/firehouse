import folium

richmond_coords = [37.53, -77.46]


def create_map(data):
    """ Generate a LeafletJS div section using Python Folium. """
    m = folium.Map(location=richmond_coords)
    lat, lon = data['address']['latitude'], data['address']['longitude']
    address_line1 = data['address']['address_line1']
    folium.Marker([lat, lon], popup=address_line1).add_to(m)
    return m._repr_html_()
