// // Miami coordinates 25.775080 -80.194702
// // Create an array of markers for each restaurant in the data.js file
// let restaurantMarker = [];

// for (let i = 0; i < restaurants.length; i++) {
//   restaurantMarker.push(
//     L.marker(restaurants[i].location).bindPopup(`
//     <h1>${restaurants[i].name}</h1><hr>
//     <h3>Category: ${restaurants[i].category}</h3><br/>
//     <h3>Rating: ${restaurants[i].rating}</h3><br/>
//     <h3>Address: ${restaurants[i].address}</h3>`)
//   );
// }

// // Add the restaurant markers to a new layer
// let streetMap = L.tileLayer(
//   "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
//   {
//     attribution:
//       '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
//   }
// );

// let restaurantLocations = [];

// let locations = L.layerGroup(restaurantLocations);

// let baseMaps = {
//   StreetMap: streetMap,
// };

// let overlayMaps = {
//   American: american,
//   Brazilian: brazilian,
//   CajunCreole: cajun / creole,
//   Caribbean: caribbean,
//   Cuban: cuban,
//   French: french,
//   Italian: italian,
//   Mexican: mexican,
//   Steakhouses: steakhouses,
// };

// // Create a map object, and set the default layers.
// let myMap = L.map("map", {
//   center: [25.77508, -80.194702],
//   zoom: 6,
//   layers: [
//     streetMap,
//     american,
//     brazilian,
//     cajun / creole,
//     caribbean,
//     cuban,
//     french,
//     italian,
//     mexican,
//     steakhouses,
//   ],
// });

// L.control.layers(baseMaps, overlayMaps).addTo(myMap);

// // Make map only show after clicking modal button
// const modalBtn = document.getElementById("modalBtn");
// const mapShow = document.getElementById("map");

// modalBtn.addEventListener("click", function () {
//   if (mapShow.style.display == "none") {
//     mapShow.style.display == "block";
//   } else {
//     mapShow.style.display == "none";
//   }
// });

// Creating our initial map object:
// We set the longitude, latitude, and starting zoom level.
// This gets inserted into the div with an id of "map".
let myMap = L.map("map", {
  center: [25.77508, -80.194702],
  zoom: 13,
});

// Adding a tile layer (the background map image) to our map:
// We use the addTo() method to add objects to our map.
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(myMap);
