from geopy.geocoders import Nominatim
from graphh import graphhopper

class GraphHopperExtended(graphhopper.GraphHopper):
    def route_3d(self, start_point, end_point):
        response = self.route(start_point, end_point, vehicle='car')
        return response.json()['paths'][0]['points']

geolocator = Nominatim(user_agent="myapp")
gh = GraphHopperExtended(api_key='b728c147-9404-445b-940f-270b9e50de7c')

def get_route(destination):
    start_loc = geolocator.geocode("current location")
    start_point = (start_loc.latitude, start_loc.longitude)

    end_loc = geolocator.geocode(destination)
    end_point = (end_loc.latitude, end_loc.longitude)

    return gh.route_3d(start_point, end_point)