

import tkinter as tk
from tkinter import ttk
import folium
from geopy.geocoders import Nominatim

# Initialize map 
map = folium.Map(location=[20, 0], zoom_start=2)

# Initialize Nominatim geocoder
geocoder = Nominatim(user_agent="myapp")

# Initialize GUI
root = tk.Tk()

def search():
    location = entry.get()
    location = geocoder.geocode(location)

    popup = folium.Popup(location[0], max_width=300)
    folium.Marker([location.latitude, location.longitude], popup=popup).add_to(map)
    
    map.location = [location.latitude, location.longitude]

entry = ttk.Entry(root)
entry.grid(row=0, column=0)

search_btn = ttk.Button(root, text="Search", command=search)
search_btn.grid(row=0, column=1)

# Display map
map.add_to(root)

root.mainloop()