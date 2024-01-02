import tkinter as tk
from tkinter import ttk
import cesium_map 
from mapbox_impl import set_api_keys, create_mapbox_map, create_mapbox_directions, create_mapbox_geocoder
import iPython

# Mapbox access token
mapbox_access_token = 'pk.eyJ1IjoidGFyaXFiaXZpamkiLCJhIjoiY2xsNTY0d3JtMGQxdjNlbzF2b2loNm40aCJ9.AZajFCsj0ImNT2zgkcF45Q'

# Set API keys 
set_api_keys(mapbox_access_token)

# Create Cesium viewer
cesium_viewer = cesium_map.create_cesium_viewer()

# Create Mapbox map
mapbox_map = create_mapbox_map()  

# Create Directions 
directions = create_mapbox_directions()

# Create Geocoder
mapbox_geocoder = create_mapbox_geocoder(mapbox_access_token)

# Initialize maps
def initialize():
  current_loc = mapbox_geocoder.geocode('Current Location').geometry() 

  cesium_map.fly_to_coordinates(cesium_viewer, current_loc)

  mapbox_map.set_view(current_loc)

# Handle search 
def search():
  destination = entry.get()

  if destination:
    destination_loc = mapbox_geocoder.geocode(destination).geometry()

    cesium_map.fly_to_coordinates(cesium_viewer, destination_loc)

    directions.set_destination(destination_loc)
    mapbox_map.draw_route(directions)
    
# Create UI
root = tk.Tk()
entry = ttk.Entry(root)
entry.pack()

search_btn = ttk.Button(root, text="Search", command=search) 
search_btn.pack()

# Initialize
initialize()

root.mainloop()