/**
 * Google maps additional functions
 */

/**
 * Takes a JSON'ed picture object and adds a marker to the map
 * at the correct location with an info-window containing
 * information about the picture and the picture itself.
 * @param pictureObj
 */
google.maps.Map.prototype.addMarkerFromJson = function(pictureObj) {
    var map = this
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

/**
 * Takes a JSON object and gets any picture objects
 * within it, then calls the add marker function.
 * @param jsonObj
 */
google.maps.Map.prototype.getPictureDataFromJson = function (jsonObj) {
    if (jsonObj.hasOwnProperty("pictures")) {
        var pictureList = jsonObj.pictures
        for (var i=0; i < pictureList.length; i++) {
            this.addMarkerFromJson(pictureList[i]);
        }
    }
}

/**
 * Clears all the markers on the map.
 */
google.maps.Map.prototype.clearMarkers = function() {
    if (!this.hasOwnProperty("markers")) {
        this.markers = new Array();
    }
    for(var i=0; i < this.markers.length; i++){
        this.markers[i].setMap(null);
    }
    this.markers = new Array();
};

/**
 * Takes the fields to be populated with the coordinates, and
 * adds a right-click event to the map that adds a new marker
 * and places the co-ordinates of the click in the fields.
 * @param latField
 * @param lngField
 */
google.maps.Map.prototype.locationPicker = function(latField, lngField) {
    google.maps.event.addListener(this, "rightclick", function(event) {
        var lat = parseFloat(event.latLng.lat()).toFixed(8);
        var lng = parseFloat(event.latLng.lng()).toFixed(8);
        latField.val(lat);
        lngField.val(lng);
        this.clearMarkers();
        var location = new google.maps.LatLng(lat, lng)
        var marker = new google.maps.Marker({
            title: "Your picture!",
            position: location,
            map: this
        });
        this.markers.push(marker);
    });
}