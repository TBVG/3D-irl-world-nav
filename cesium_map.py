import cesiumpy

class CesiumNavigationApp:
    def __init__(self):
        self.viewer = cesiumpy.Viewer()
        self.route_layer = cesiumpy.PolylineCollection()

    def add_route_to_map(self, route):
        cesiumpy.Polyline(
            positions=route,
            width=5,
            material=cesiumpy.Color.from_alpha(cesiumpy.Color.RED, 0.7),
        ).add_to(self.route_layer)
        self.route_layer.add_to(self.viewer)

    def fly_to_coordinates(self, coordinates):
        self.viewer.camera.flyTo(
            cesiumpy.Cartesian3.fromDegrees(*coordinates, height=10000000)
        )

    def start_navigation(self):
        self.viewer.render()