function addMarker(pictureObj, map) {
    var location = new google.maps.LatLng(pictureObj.latitude, pictureObj.longitude)
    var marker = new google.maps.Marker({
        title: pictureObj.title,
        position: location,
        map: map
    });
}

function addMarkersFromJson(jsonObj, map) {
    if (jsonObj.hasOwnProperty("pictures")) {
        var pictureList = jsonObj.pictures
        for (var i=0; i < pictureList.length; i++) {
            addMarker(pictureList[i], map);
        }
    }
}