import cesiumpy

def create_cesium_viewer():
  return cesiumpy.Viewer()

def fly_to_coordinates(viewer, coordinates):
  viewer.camera.flyTo(cesiumpy.Cartesian3.fromDegrees(*coordinates, height=10000000))