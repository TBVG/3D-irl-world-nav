import asyncio
from geopy.asyncio import Nominatim
from graphh import graphhopper
from config import Config
from logger import app_logger

class GraphHopperExtended(graphhopper.GraphHopper):
    """
    Extends the GraphHopper class to include 3D routing.
    """

    def route_3d(self, start_point, end_point):
        """
        Retrieves a 3D route from the start point to the end point.
        
        :param start_point: Tuple representing the starting coordinates (latitude, longitude).
        :param end_point: Tuple representing the ending coordinates (latitude, longitude).
        :return: List of [longitude, latitude] pairs representing the route, or an empty list on failure.
        """
        try:
            response = self.route(start_point, end_point, vehicle='car')
            response.raise_for_status()
            return response.json()['paths'][0]['points']['coordinates']
        except Exception as e:
            app_logger.error(f"Failed to retrieve 3D route: {e}")
            return []

async def async_geocode(geolocator, location):
    """
    Asynchronously geocodes a location using the provided geolocator.
    
    :param geolocator: Instance of the geolocator to use for geocoding.
    :param location: The location to geocode (address, place name, etc.).
    :return: The geocoded location or None if an error occurs.
    """
    try:
        return await geolocator.geocode(location)
    except Exception as e:
        app_logger.error(f"Geocoding error: {e}")
        return None

async def get_route(destination):
    """
    Retrieves the route from the current location to the destination using geocoding and GraphHopper.
    
    :param destination: The destination to which the route should be calculated.
    :return: The 3D route as a list of [longitude, latitude] pairs or an empty list on failure.
    """
    geolocator = Nominatim(user_agent="myapp")
    gh = GraphHopperExtended(api_key=Config.GRAPHHOPPER_API_KEY)

    # Geocode the current location asynchronously
    start_loc = await async_geocode(geolocator, "current location")
    if not start_loc:
        app_logger.error("Could not determine the current location.")
        return []

    start_point = (start_loc.latitude, start_loc.longitude)

    # Geocode the destination asynchronously
    end_loc = await async_geocode(geolocator, destination)
    if not end_loc:
        app_logger.error(f"Could not determine the location for {destination}.")
        return []

    end_point = (end_loc.latitude, end_loc.longitude)
    
    # Retrieve the 3D route between the start and end points
    return gh.route_3d(start_point, end_point)
