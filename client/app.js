function getFurnValue() {
  var uiFurnish = document.getElementsByName("uiFurnish");
  for(var i in uiFurnish) {
    if(uiFurnish[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimateRent() {
  console.log("Estimate rent button clicked");
  var sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var furnish = getFurnValue();
  var location = document.getElementById("uiLocations");
  var estRent = document.getElementById("uiEstimatedRent");

  var url = "http://127.0.0.1:5000/predict_house_rent"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_house_rent"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      total_sqft: parseFloat(sqft.value),
      bhk: bhk,
      furnish: furnish,
      location: location.value
  },function(data, status) {
      console.log(data.estimated_rent);
      estRent.innerHTML = "<h2>" + data.estimated_rent.toString() + " Rs/Month</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;