// Initialize the Cesium viewer in the HTML container
var viewer = new Cesium.Viewer('cesiumContainer');

/**
 * Adds a route to the Cesium map as a polyline.
 * @param {Array} route - Array of [longitude, latitude] pairs representing the route.
 */
function addRouteToMap(route) {
    if (!route || route.length === 0) {
        console.error("No route data provided.");
        return;
    }

    // Convert route coordinates to Cesium Cartesian3 format
    var positions = route.map(function(coord) {
        return Cesium.Cartesian3.fromDegrees(coord[0], coord[1]);
    });

    // Add the polyline to the Cesium viewer
    viewer.entities.add({
        polyline: {
            positions: positions,
            width: 5,
            material: Cesium.Color.RED.withAlpha(0.7)
        }
    });
    console.log("Route added to map.");
}

/**
 * Flies the camera to the specified coordinates.
 * @param {Array} coordinates - [longitude, latitude] pair representing the target location.
 */
function flyToCoordinates(coordinates) {
    if (!coordinates || coordinates.length < 2) {
        console.error("Invalid coordinates provided.");
        return;
    }

    // Move the camera to the specified coordinates
    viewer.camera.flyTo({
        destination: Cesium.Cartesian3.fromDegrees(coordinates[0], coordinates[1], 1000)
    });
    console.log("Flying to coordinates.");
}

/**
 * Starts rendering the Cesium viewer.
 */
function startNavigation() {
    viewer.render();
    console.log("Navigation started.");
}

/**
 * Toggles the camera perspective between 2D and 3D views.
 */
function toggleCameraPerspective() {
    viewer.scene.camera.toggleColumbusView();
    console.log("Camera perspective toggled.");
}
