

from geopy.geocoders import Nominatim

geocoder = Nominatim(user_agent="myapp")

def geocode(location):
    return geocoder.geocode(location)