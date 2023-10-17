$(document).ready(function () {
  // Miami coordinates 25.775080 -80.194702
  // Set the base layer of the map
  // Wait for the modal to be shown
  $("#staticBackdrop1").on("shown.bs.modal", function () {
    // Create the map inside the modal
    let myMap = L.map("map", {
      center: [25.77508, -80.194702],
      zoom: 13,
    });

    // Adding a tile layer (the background map image) to the map
    let streetMap = L.tileLayer(
      "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      {
        attribution:
          '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      }
    ).addTo(myMap);

    // Load JSON data using D3
    d3.json("resources/locations.json").then(function (data) {
      // Create layers for different types of features
      let restaurantLayer = L.layerGroup();
      let fastFoodLayer = L.layerGroup();
      let supermarketLayer = L.layerGroup();

      // Create marker clusters for each category
      let restaurantCluster = L.markerClusterGroup();
      let fastFoodCluster = L.markerClusterGroup();
      let supermarketCluster = L.markerClusterGroup();

      // Loop through the data and add markers to appropriate layers with Font Awesome icons
      data.features.forEach(function (feature) {
        let coordinates = feature.geometry.coordinates;
        let properties = feature.properties;

        let markerOptions = {
          icon: L.divIcon({
            className: "custom-marker",
            html: properties.categories.includes("catering.restaurant")
              ? '<i class="fas fa-utensils" style="color: #FF0000;"></i>' // Fork and knife icon for restaurant (red color)
              : properties.categories.includes("catering.fast_food")
              ? '<i class="fas fa-hamburger" style="color: #0000FF;"></i>' // Hamburger icon for fast food (blue color)
              : properties.categories.includes("commercial.supermarket")
              ? '<i class="fas fa-shopping-cart" style="color: #66b447;"></i>' // Shopping cart icon for supermarket (green color)
              : "", // Empty string if no category matches
          }),
        };

        // Check the type of feature and add marker to the corresponding layer with Font Awesome icon
        if (properties.categories.includes("catering.restaurant")) {
          L.marker([coordinates[1], coordinates[0]], markerOptions)
            .bindPopup(
              `<h5>${
                properties.address_line1
              }</h5><hr><strong>Address: </strong>${
                properties.address_line2
              }<br><br><strong>Category: </strong>${
                properties.categories.includes("catering.restaurant")
                  ? "Restaurant"
                  : properties.categories.includes("catering.fast_food")
                  ? "Fast Food"
                  : properties.categories.includes("commercial.supermarket")
                  ? "Supermarket"
                  : ""
              }`
            )
            .addTo(restaurantLayer);
        } else if (properties.categories.includes("catering.fast_food")) {
          L.marker([coordinates[1], coordinates[0]], markerOptions)
            .bindPopup(
              `<h5>${
                properties.address_line1
              }</h5><hr><strong>Address: </strong>${
                properties.address_line2
              }<br><br><strong>Category: </strong>${
                properties.categories.includes("catering.restaurant")
                  ? "Restaurant"
                  : properties.categories.includes("catering.fast_food")
                  ? "Fast Food"
                  : properties.categories.includes("commercial.supermarket")
                  ? "Supermarket"
                  : ""
              }`
            )
            .addTo(fastFoodLayer);
        } else if (properties.categories.includes("commercial.supermarket")) {
          L.marker([coordinates[1], coordinates[0]], markerOptions)
            .bindPopup(
              `<h5>${
                properties.address_line1
              }</h5><hr><strong>Address: </strong>${
                properties.address_line2
              }<br><br><strong>Category: </strong>${
                properties.categories.includes("catering.restaurant")
                  ? "Restaurant"
                  : properties.categories.includes("catering.fast_food")
                  ? "Fast Food"
                  : properties.categories.includes("commercial.supermarket")
                  ? "Supermarket"
                  : ""
              }`
            )
            .addTo(supermarketLayer);
        }

        // Check the type of feature and add marker to the corresponding cluster
        if (properties.categories.includes("catering.restaurant")) {
          let marker = L.marker([coordinates[1], coordinates[0]]);
          restaurantCluster.addLayer(
            marker.bindPopup(
              `<h5>${
                properties.address_line1
              }</h5><hr><strong>Address: </strong>${
                properties.address_line2
              }<br><br><strong>Category: </strong>${
                properties.categories.includes("catering.restaurant")
                  ? "Restaurant"
                  : properties.categories.includes("catering.fast_food")
                  ? "Fast Food"
                  : properties.categories.includes("commercial.supermarket")
                  ? "Supermarket"
                  : ""
              }`
            )
          );
        } else if (properties.categories.includes("catering.fast_food")) {
          let marker = L.marker([coordinates[1], coordinates[0]]);
          fastFoodCluster.addLayer(
            marker.bindPopup(
              `<h5>${
                properties.address_line1
              }</h5><hr><strong>Address: </strong>${
                properties.address_line2
              }<br><br><strong>Category: </strong>${
                properties.categories.includes("catering.restaurant")
                  ? "Restaurant"
                  : properties.categories.includes("catering.fast_food")
                  ? "Fast Food"
                  : properties.categories.includes("commercial.supermarket")
                  ? "Supermarket"
                  : ""
              }`
            )
          );
        } else if (properties.categories.includes("commercial.supermarket")) {
          let marker = L.marker([coordinates[1], coordinates[0]]);
          supermarketCluster.addLayer(
            marker.bindPopup(
              `<h5>${
                properties.address_line1
              }</h5><hr><strong>Address: </strong>${
                properties.address_line2
              }<br><br><strong>Category: </strong>${
                properties.categories.includes("catering.restaurant")
                  ? "Restaurant"
                  : properties.categories.includes("catering.fast_food")
                  ? "Fast Food"
                  : properties.categories.includes("commercial.supermarket")
                  ? "Supermarket"
                  : ""
              }`
            )
          );
        }
      });

      // Create a new layer for all locations with marker clusters
      let allLocationsClusterLayer = L.layerGroup([
        restaurantCluster,
        fastFoodCluster,
        supermarketCluster,
      ]);

      // Add layers to the map with different colors
      let baseLayers = {
        "Street Map": streetMap,
      };

      let overlayLayers = {
        Restaurants: restaurantLayer.addTo(myMap),
        "Fast Food": fastFoodLayer.addTo(myMap),
        Supermarkets: supermarketLayer.addTo(myMap),
        "All Locations Cluster": allLocationsClusterLayer,
      };

      L.control
        .layers(baseLayers, overlayLayers, {
          collapsed: false,
        })
        .addTo(myMap);

      // Define FontAwesome icons and their colors
      const legendIcons = {
        "fas fa-utensils": "#FF0000", // Restaurant icon with red color
        "fas fa-hamburger": "#0000FF", // Fast food icon with green color
        "fas fa-shopping-cart": "#66b447", // Supermarket icon with blue color
      };

      // Function to get layer name by FontAwesome icon class
      function getLayerNameByIconClass(iconClass) {
        switch (iconClass) {
          case "fas fa-utensils":
            return "Restaurants";
          case "fas fa-hamburger":
            return "Fast Food";
          case "fas fa-shopping-cart":
            return "Supermarkets";
          default:
            return "";
        }
      }

      // Create a custom legend control
      const legend = L.control({ position: "bottomright" });

      legend.onAdd = function (map) {
        let div = L.DomUtil.create("div", "legend");
        div.innerHTML += "<h6>Category Icons</h6>";
        for (const [iconClass, color] of Object.entries(legendIcons)) {
          const legendItem = L.DomUtil.create("div", "legend-item", div);
          legendItem.innerHTML =
            `<i class="${iconClass} legend-icon" style="color: ${color};"></i>` +
            `<span class="legend-text">${getLayerNameByIconClass(
              iconClass
            )}</span>`;
        }
        return div;
      };

      // Add the legend control to the map
      legend.addTo(myMap);
    });
  });
});
