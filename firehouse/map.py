import folium

richmond_coords = [37.53, -77.46]


def create_popup(data):
    address_line1 = data['address']['address_line1']
    event_opened = data['description']['event_opened']
    date, time = event_opened.split('T')
    year, month, day = date.split('-')
    hour, minute = time.split(':')[:2]
    _type = data['description']['type']
    subtype = data['description']['subtype']
    weather = data['weather'][int(hour)]['Conditions']
    parcel = data['parcel']['spatialReference']['wkid']
    stations = [x['station'] for x in data['apparatus']]
    stations = ', '.join(list(set(stations)))
    popup = f"""
        <h4>{address_line1}</h4>
        <h5>{date} {hour}:{minute}<h5>
        <code>{_type}: {subtype}</code>
        <p>Weather: {weather}</p>
        <p>Parcel: {parcel}</p>
        <p>Stations involved: {stations}</p>
        """
    return popup


def create_map(data):
    """ Generate a LeafletJS div section using Python Folium. """
    m = folium.Map(location=richmond_coords)
    lat, lon = data['address']['latitude'], data['address']['longitude']
    popup = create_popup(data)
    folium.Marker([lat, lon], popup=popup).add_to(m)
    return m._repr_html_()
