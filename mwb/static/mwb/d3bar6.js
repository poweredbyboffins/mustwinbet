function d3bar(roundag)
{


var data = [];
var res = 0;
//var obj {};

for (var i=0; i < 6;i++)
           {
            res=poisson(i,roundag);
            res=Math.round(res);
            data.push({ goals : i,
                    value : res
                  });
           }

// Set the dimensions of the canvas / graph
var	margin = {top: 30, right: 20, bottom: 30, left: 50},
	width = 400 - margin.left - margin.right,
	height = 220 - margin.top - margin.bottom;

// Parse the date / time
var	parseDate = d3.time.format("%d-%b-%y").parse;

// Set the ranges
var	x = d3.time.scale().range([0, width]);
var	y = d3.scale.linear().range([height, 0]);

// Define the axes
var	xAxis = d3.svg.axis().scale(x)
	.orient("bottom").ticks(5);

var	yAxis = d3.svg.axis().scale(y)
	.orient("left").ticks(5);

// Define the line
var	valueline = d3.svg.line()
	.x(function(d) { return x(d.goals); })
	.y(function(d) { return y(d.value); });
    
// Adds the svg canvas
var	chart1 = d3.select("body")
	.append("svg")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
	.append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Get the data
/*d3.csv("data1.csv", function(error, data) {
	data.forEach(function(d) {
		d.date = parseDate(d.date);
		d.close = +d.close;
	});
*/

	// Scale the range of the data
	x.domain(d3.extent(data, function(d) { return d.goals; }));
	y.domain([0, d3.max(data, function(d) { return d.value; })]);

	// Add the valueline path.
	chart1.append("path")
		.attr("class", "line")
		.attr("d", valueline(data));

	// Add the X Axis
	chart1.append("g")
		.attr("class", "x axis")
		.attr("transform", "translate(0," + height + ")")
		.call(xAxis);

	// Add the Y Axis
	chart1.append("g")
		.attr("class", "y axis")
		.call(yAxis);

});

// Adds the svg canvas
var	chart2 = d3.select("body")
	.append("svg")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
	.append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
		
// Get the data
/*d3.csv("data2.csv", function(error, data) {
	data.forEach(function(d) {
		d.date = parseDate(d.date);
		d.close = +d.close;
	});
*/
	// Scale the range of the data
	x.domain(d3.extent(data, function(d) { return d.goals; }));
	y.domain([0, d3.max(data, function(d) { return d.value; })]);

	// Add the valueline path.
	chart2.append("path")
		.attr("class", "line")
		.attr("d", valueline(data));

	// Add the X Axis
	chart2.append("g")
		.attr("class", "x axis")
		.attr("transform", "translate(0," + height + ")")
		.call(xAxis);

	// Add the Y Axis
	chart2.append("g")
		.attr("class", "y axis")
		.call(yAxis);

//});

}
