

**Title:** Mapping Food Insecurity: A Study of Miami's Food Deserts<br/>
**Project 3, Group 5**<br/>
**Contributors:** Alexandra Calametti, Brian Kath, Laura Bishop and Noah McHale<br/>
<!-- PDF of  Presentation found here. (( Linke to HTML? -->


## Introduction:
<img src="https://github.com/brnkath/project-3-group-5/blob/main/img/miami-1.jpg">
In the vibrant city of Miami, Florida, known for its stunning beaches, diverse culture, and lively atmosphere, a less visible but pressing issue silently affects the lives of many of its residents: food deserts. “Food Desert” is a term used to describe an area where access to fresh, nutritious, and affordable food is severely limited or non-existent. This issue is not unique to Miami, but it is particularly pronounced in Miami-Dade County, where a complex web of socio-economic factors, urban development, and geographic disparities has left a significant portion of its population struggling to find access to the basic necessity of wholesome, nourishing food.<br/>

In this project, we will investigate the concept of food deserts, exploring their definition, their impact on the health and well-being of Miami's communities, and why Miami-Dade County serves as a poignant case study for the challenges associated with food deserts. Through an analysis of available data, we aim to illuminate this critical issue, gaining insight into its underlying causes and consequences, with the ultimate goal of working towards a more equitable and nourished future for all Miami residents.<br/>

We used a ‘drill down’ approach, beginning with the State of Florida, into Miami-Dade County, until eventually localizing on the City of Miami.<br/>

### What Can Be Done:
<img src="https://github.com/brnkath/project-3-group-5/blob/main/img/miami-striking-for-better-wages-small.png" align="left">
Addressing the food desert crisis in Miami, while also tackling income disparity, requires a multi-faceted approach that recognizes the interconnected nature of these issues. <br/>

First and foremost, local and state governments must invest in targeted policies that promote economic equity. This includes raising the minimum wage, providing job training and educational opportunities, and supporting affordable housing initiatives. By addressing income disparities, more residents will have the means to access fresh and nutritious food, reducing the reliance on fast food outlets and convenience stores as primary sources of sustenance.<br/>

Simultaneously, community-based initiatives are crucial to improving food access in underserved neighborhoods. Supporting the development of community gardens, urban farms, and farmers' markets in these areas can provide residents with affordable, locally-sourced produce.<br/>

Collaborations between local businesses, nonprofits, and government agencies can further enhance access to healthy food options. Education and outreach programs can also play a pivotal role in empowering residents to make healthier dietary choices. By addressing income disparities and implementing community-driven solutions, Miami can work towards mitigating the food desert crisis, improving the overall well-being of its residents, and fostering a more equitable and sustainable future for all.

## The Project:

### Sources & Resources:

  * United States Census Bureau: https://www.census.gov/
  * Miami Matters - Measuring What Matters in Miami-Dade County: Miami-Dade Matters: https://www.miamidadematters.org/
  * Places API Playground: https://apidocs.geoapify.com/playground/places/
  * State-zip-code-GeoJSON courtesy of Git Hub’s <a href="https://github.com/enactdev">enactdev</a> (part of the 
<a href="https://github.com/OpenDataDE">Open Data Delaware Project</a>): https://github.com/OpenDataDE/State-zip-code-GeoJSON

### Additional Took Kits:
  * Jombotron courtesy of mdbootstrap.com: https://mdbootstrap.com/docs/standard/extended/jumbotron 
  * Hidden API Link div courtesy of jQuery toggle feature: https://www.w3schools.com/jquery/eff_toggle.asp
  * API tab section courtesy of W3schools: https://www.w3schools.com/howto/howto_js_tabs.asp
  * SQLite Viewer Web App: https://sqliteviewer.app/ 

### The Map:
<img src="https://github.com/brnkath/project-3-group-5/blob/main/img/map_image.png" align="left" width="75%">

The main thrust of our project’s presentation is our map. 

The map is located within a Bootstrap modal that opens when the “Map of Locations” button from the main page is clicked. The initial view that displays when the map is loaded shows a zoomed-in map of the Miami, Florida area. There is one base layer that uses the street map version from openstreetmap.org. Additionally, there are a total of eight overlay layers. Four layers immediately show when the map loads. These layers include individual layers for each location category from our dataset (Restaurants, Fast Food, and Supermarkets) with customized icons for each location/location category. Each location icon also includes a popup when clicked that shows the name of the location, the address, and the category that the location belongs to. 

The fourth layer that shows up when the map loads include the boundaries of the zip codes surrounding the city of Miami. Each zip code includes a popup when clicked that lists the specific zip code and the median income within that zip code. The background colors of the zip codes are based on the median income. There are also two legends in the map that show the color range related to the median income of each zip code, and the icons associated with each location category.

The four additional layers that can be seen by clicking the checkboxes in the controls at the upper right corner of the map include individual layers of marker clusters for each location category. These marker cluster layers group up the locations for each category to make it easier to see where the locations for each category are concentrated. The final layer that can be used shows a boundary line of the city of Miami. This layer can make it easier to see how the zip codes specific to Miami differ from the surrounding zip codes regarding median income.

### Visualizations:

<table>
  <tr>
    <th>Bar Chart</th>
    <th>Pie Chart</th>
  </tr>
  <tr>
    <td><img src="https://github.com/brnkath/project-3-group-5/blob/main/img/miami-dade-zipcode-income-bargraph.png"></td>
    <td><img src="https://github.com/brnkath/project-3-group-5/blob/main/img/avail-food-source-piechart.png"></td>
  </tr>
  <tr>
    <td>Bar chart of the income spectrum with data from the US Census Bureau, broken out by zip code</td>
    <td>Pie chart showing the food resources available to the City of Miami, as defined by zip code</td>
  </tr>
</table>

### Directory of Files:

 **Folders:**<br/>
  * <a href="https://github.com/brnkath/project-3-group-5/tree/main/css">CSS</a> - CSS files<br/>
  * <a href="https://github.com/brnkath/project-3-group-5/tree/main/img">img</a> - Image files used throughout the project<br/>
  * <a href="https://github.com/brnkath/project-3-group-5/tree/main/js">js</a> - JavaScript files<br/>
  * <a href="https://github.com/brnkath/project-3-group-5/tree/main/resources">resources</a> - Juypter Notebooks, CSV, JSON, geoJSON files<br/>
  * <a href="https://github.com/brnkath/project-3-group-5/tree/main/templates">templates</a> - Flask files<br/>
