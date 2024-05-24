// cesium_navigation.js
var viewer = new Cesium.Viewer('cesiumContainer');

function addRouteToMap(route) {
    var polyline = new Cesium.PolylineGraphics({
        positions: Cesium.Cartesian3.fromDegreesArray(route),
        width: 5,
        material: Cesium.Color.RED.withAlpha(0.7)
    });
    viewer.entities.add({
        polyline: polyline
    });
}

function flyToCoordinates(coordinates) {
    viewer.camera.flyTo({
        destination: Cesium.Cartesian3.fromDegrees(coordinates[0], coordinates[1], 10000000)
    });
}

function startNavigation() {
    viewer.render();
}