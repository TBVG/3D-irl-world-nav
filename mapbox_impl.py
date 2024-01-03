import mapbox
from mapbox import Geocoder, Directions
import mapboxgl
access_token = 'pk.eyJ1IjoidGFyaXFiaXZpamkiLCJhIjoiY2xsNTY0d3JtMGQxdjNlbzF2b2loNm40aCJ9.AZajFCsj0ImNT2zgkcF45Q'
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