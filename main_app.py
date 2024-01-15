import tkinter as tk
from tkinter import ttk
from cesium_map import CesiumNavigationApp
from routing import get_route, GraphHopper

class NavigationAppGUI:
    def __init__(self, cesium_app):
        self.cesium_app = cesium_app
        self.root = tk.Tk()
        self.setup_ui()

    def setup_ui(self):
        entry = ttk.Entry(self.root)
        entry.grid(row=0, column=0)

        search_btn = ttk.Button(
            self.root, text="Search", command=lambda: self.search(entry.get())
        )
        search_btn.grid(row=0, column=1)

        self.root.mainloop()

    def search(self, destination):
        route = get_route(destination)
        self.cesium_app.add_route_to_map(route)
        self.cesium_app.fly_to_coordinates(route[0])
