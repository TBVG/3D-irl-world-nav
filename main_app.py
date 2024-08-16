import tkinter as tk
from tkinter import ttk, messagebox
from cesium_navigation import CesiumNavigationApp
import asyncio
from routing import get_route
from logger import app_logger

class NavigationAppGUI:
    """
    Class to manage the GUI for the 3D navigation app.
    """

    def __init__(self, cesium_app):
        """
        Initializes the GUI with a reference to the Cesium app.
        
        :param cesium_app: Instance of CesiumNavigationApp for interacting with the Cesium map.
        """
        self.cesium_app = cesium_app
        self.root = tk.Tk()
        self.root.title("3D Navigation App")
        self.setup_ui()

    def setup_ui(self):
        """
        Sets up the user interface elements, including entry fields and buttons.
        """
        tk.Label(self.root, text="Enter Destination:").grid(row=0, column=0, padx=5, pady=5)

        self.entry = ttk.Entry(self.root, width=30)
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        search_btn = ttk.Button(self.root, text="Search", command=self.search)
        search_btn.grid(row=0, column=2, padx=5, pady=5)

        toggle_camera_btn = ttk.Button(self.root, text="Toggle Camera", command=self.toggle_camera_perspective)
        toggle_camera_btn.grid(row=0, column=3, padx=5, pady=5)

        self.loading_label = tk.Label(self.root, text="")
        self.loading_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        self.root.mainloop()

    def search(self):
        """
        Initiates the search for a route based on the destination entered by the user.
        """
        destination = self.entry.get()
        if not destination:
            messagebox.showwarning("Input Error", "Please enter a destination.")
            return

        # Display loading message while fetching the route
        self.loading_label.config(text="Loading route, please wait...")
        
        # Execute the route search asynchronously
        self.root.after(100, self.async_search, destination)

    def async_search(self, destination):
        """
        Runs the route search asynchronously.
        
        :param destination: The destination to which the route should be calculated.
        """
        asyncio.run(self.search_route(destination))

    async def search_route(self, destination):
        """
        Asynchronously searches for a route and displays it on the map.
        
        :param destination: The destination to which the route should be calculated.
        """
        try:
            # Fetch the route asynchronously
            route = await get_route(destination)
            if route:
                # Display the route on the Cesium map
                self.cesium_app.add_route_to_map(route)
                self.cesium_app.fly_to_coordinates(route[0])
                self.cesium_app.start_navigation()
                messagebox.showinfo("Success", "Route loaded successfully!")
            else:
                messagebox.showerror("Error", "Failed to retrieve route.")
        except Exception as e:
            # Log and display any errors encountered
            app_logger.error(f"Search error: {e}")
            messagebox.showerror("Error", str(e))
        finally:
            # Clear the loading message
            self.loading_label.config(text="")

    def toggle_camera_perspective(self):
        """
        Toggles the camera perspective between 2D and 3D views in the Cesium map.
        """
        self.cesium_app.toggle_camera_perspective()
