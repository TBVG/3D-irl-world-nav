from cesium_navigation_app import CesiumNavigationApp
from navigation_app_gui import NavigationAppGUI

# Run the app
cesium_app = CesiumNavigationApp()
gui_app = NavigationAppGUI(cesium_app)
cesium_app.start_navigation()
