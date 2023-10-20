// Start Miami-Dade County Median Income by Zip Code Bar Graph

// Fetch the miami_info.csv
fetch("resources/miami_info.csv")
  .then((response) => response.text())
  .then((data) => processData(data));

function processData(data) {
  // Parse the CSV data into an array of objects
  const parsedData = d3.csvParse(data, (d) => ({
    Zipcode: d.Zipcode.toString(), // Convert Zipcode to a string
    Median_income: +d.Median_income.replace(/\$/, "").replace(/,/g, ""), // Convert Median_income to a number
  }));

  // Extract the Zipcode and Median_income data
  const zipcodes = parsedData.map((item) => item.Zipcode);
  const incomes = parsedData.map((item) => item.Median_income);

  // Create the Plotly bar graph
  createBarGraph(zipcodes, incomes);
}

const trace = {
  x: zipcodes, // X-axis should be Zipcodes
  y: incomes, // Y-axis should be Median_income
  type: "bar",
  marker: {
    color: "orange", // Set the bar color to Orange
  },
};

// Reference: https://plotly.com/python/reference/layout/xaxis/
// Reference: https://plotly.com/javascript/bar-charts/

function createBarGraph(zipcodes, incomes) {
  const trace = {
    x: zipcodes, // X-axis should be Zipcodes
    y: incomes, // Y-axis should be Median_income
    type: "bar",
    marker: {
      color: "orange", // Set the bar color to orange
    },
  };

  const layout = {
    title: "Miami-Dade County Median Income by Zip Code",
    xaxis: {
      title: "Zip Code",
      type: "category", // Set the X-axis type to 'category'
      tickmode: "linear", // Set the tick mode to 'linear' to preserve the original Zipcodes
      tickangle: -45, // Set the angle of the tick to -45 degrees
    },
    yaxis: { title: "Median Income" },
  };

  Plotly.newPlot("bar-graph", [trace], layout);
}

// End Miami-Dade County Median Income by Zip Code Bar Graph

// Start Pie Chart of Available Food Sources

fetch("resources/cat_breakdown.csv")
  .then((response) => response.text())
  .then((data) => {
    // Split the CSV data into rows
    const rows = data.split("\n");

    // Extract the header and split it into column names
    const header = rows[0].split(",");
    const labelsIndex = header.indexOf("Category");
    const valuesIndex = header.indexOf("Count");

    // Initialize arrays to store labels and values
    const labels = [];
    const values = [];

    // Iterate through the rows and extract data
    for (let i = 1; i < rows.length; i++) {
      const columns = rows[i].split(",");
      if (columns.length >= valuesIndex + 1) {
        labels.push(columns[labelsIndex]);
        values.push(parseInt(columns[valuesIndex], 10));
      }
    }

    let trace = {
      type: "pie",
      labels: labels,
      values: values,
    };

    let layout = {
      title: "Available Food Sources",
    };

    let config = {
      responsive: true,
    };

    Plotly.newPlot("pie-chart", [trace], layout, config);
  });

// End Pie Chart of Available Food Sources
