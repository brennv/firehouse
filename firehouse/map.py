import folium
import os

richmond_coords = [37.53, -77.46]


def create_map():
    """Takes a folium instance and embed HTML."""
    m = folium.Map(location=richmond_coords)
    return m._repr_html_()
