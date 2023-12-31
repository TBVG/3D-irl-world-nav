import mapbox
from mapbox import Geocoder, Directions
import mapboxgl

# Set access token
def set_api_keys(access_token):
  mapbox.access_token = access_token

def create_mapbox_map():
  return mapboxgl.Map()

def create_mapbox_directions():
  return Directions()

# Pass access token
def create_mapbox_geocoder(access_token):
  return Geocoder(access_token=access_token)