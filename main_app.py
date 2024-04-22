# main_app.py
import tkinter as tk
from tkinter import ttk
from cesium_map import CesiumNavigationApp
from routing import get_route

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

        toggle_camera_btn = ttk.Button(
            self.root, text="Toggle Camera", command=self.toggle_camera_perspective
        )
        toggle_camera_btn.grid(row=0, column=2)

        self.root.mainloop()

    def search(self, destination):
        route = get_route(destination)
        self.cesium_app.add_route_to_map(route)
        self.cesium_app.fly_to_coordinates(route[0])
        self.cesium_app.start_navigation()

    def toggle_camera_perspective(self):
        # Call the toggle_camera_perspective method of CesiumNavigationApp
        self.cesium_app.toggle_camera_perspective()

def run_app():
    cesium_app = CesiumNavigationApp()
    gui_app = NavigationAppGUI(cesium_app)
    cesium_app.start_navigation()

if __name__ == "__main__":
    run_app()