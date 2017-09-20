import folium


richmond_coords = [37.53, -77.46]


def create_map():
    m = folium.Map(location=richmond_coords)
    m.save('templates/map.html')
    pass
