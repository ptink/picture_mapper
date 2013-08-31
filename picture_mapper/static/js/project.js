function addMarker(pictureObj, map) {
  var contentString = '<div id="content">' +
      '<div id="siteNotice">' +
      '</div>' +
      '<h1 id="firstHeading" class="firstHeading">' + pictureObj.title + '</h1>' +
      '<div id="bodyContent">'+
      '<img style="max-width: 400px; max-height: 300px;" src="/media/' + pictureObj.image + '" />' +
      '<p>' + pictureObj.description + '</p>' +
      '<p>Uploaded by <b>' + pictureObj.author__username + '</b> ' +
      'on <b>' + new Date(pictureObj.created).toLocaleDateString() + '</b></p>' +
      '</div>' +
      '</div>';
    var location = new google.maps.LatLng(pictureObj.latitude, pictureObj.longitude)
    var infowindow = new google.maps.InfoWindow({
        content: contentString,
        maxHeight: 300,
        maxWidth: 400
    });
    var marker = new google.maps.Marker({
        title: pictureObj.title,
        position: location,
        map: map
    });
    google.maps.event.addListener(marker, 'click', function() {
      infowindow.open(map, marker);
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