$(function(){
	function initMap() {
	  // The location of Uluru
	  var uluru = {lat: -25.344, lng: 131.036};
	  // The map, centered at Uluru
	  var map = new google.maps.Map(
	      document.getElementById('map'), {zoom: 4, center: uluru});
	  // The marker, positioned at Uluru
	  var marker = new google.maps.Marker({position: uluru, map: map});
	}
	/** if (navigator.geolocation) {

		navigator.geolocation.getCurrentPosition(getCoords, getErrot);
	}else{
		initialize(13.30272, -87.194107);
	}

	function getCoords(position){
		var lat = position.coords.latitude;
		var lng = position.coords.longitude;

		initialize(lat, lng);
	}

	function getError(err){
		initialize(13.30272, -87.194107);
	}

	function initialize(lat, lng){
		var latlng = new google.maps.Map(lat, lng);
		var mapsSettings = {
			center: latlng,
			zoom: 15,
			mapTypeId: google.maps.MapTypeId.ROADMAP,

		}

		map = new google.maps.Map($('#mapa').get(0), mapsSettings);
	}**/

	
});
