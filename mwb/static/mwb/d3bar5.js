function d3bar5(obj)
{

var homedata = [];
var awaydata = [];
var xax = [];
var res = 0;
//var obj {};

//alert("objects" + obj.length);


for (var i=0; i < 7;i++)
//for (var i=0; i < obj.length;i++)
           {
            var sq=i*i;   

            xax.push( obj[i].fields.hometeam ); 
            homedata.push({ goals : obj[i].fields.hometeam,
                    value : obj[i].fields.winprob
                  });
            awaydata.push({ goals : obj[i].fields.awayteam,
                    value : obj[i].fields.loseprob
                  });
           }
//alert("value" + sq);
            //console.log(JSON.stringify(data));


var barWidth = 60;
var width = (barWidth + 10) * homedata.length;
var height = 100;
var margin = {top: 20, right: 10, bottom: 20, left: 10};

var x = d3.scale.linear().domain([0, homedata.length]).range([0, width]);
var y = d3.scale.linear().domain([0, d3.max(homedata, function(datum) { return datum.value; })]).
  rangeRound([0, height]);

// add the canvas to the DOM
var barDemo = d3.select("#c1").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


barDemo.selectAll("rect").
  data(homedata).
  enter().
  append("svg:rect").
  attr("x", function(datum, index) { return x(index); }).
  attr("y", function(datum) { return height - y(datum.value); }).
  attr("height", function(datum) { return y(datum.value); }).
  attr("width", barWidth).
  attr("fill", function(datum) { if (datum.value > 15) {return "red";} else { return "black"; } });

barDemo.selectAll("text").
  data(homedata).
  enter().
  append("svg:text").
  attr("x", function(datum, index) { return x(index) + barWidth; }).
  attr("y", function(datum) { return height - y(datum.value); }).
  attr("dx", -barWidth/2).
  attr("dy", "1.2em").
  attr("text-anchor", "middle").
  text(function(datum) { return datum.value;}).
  attr("fill", "white");

var axisScale = d3.scale.linear()
                          .domain([0, 10])
                          .range([0, 600]);

//Create the Axis
var xAxis = d3.svg.axis()
                  .scale(axisScale)
                  .orient("bottom").ticks(10);

var xAxisGroup = barDemo.append("g")
.attr("class", "axis")
.attr("transform", "translate(0, 100)")
                              .call(xAxis);


var x = d3.scale.linear().domain([0, awaydata.length]).range([0, width]);
var y = d3.scale.linear().domain([0, d3.max(awaydata, function(datum) { return datum.value; })]).
  rangeRound([0, height]);

// add the canvas to the DOM
var barDemo = d3.select("#c3").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

barDemo.selectAll("rect").
  data(awaydata).
  enter().
  append("svg:rect").
  attr("x", function(datum, index) { return x(index); }).
  attr("y", function(datum) { return height - y(datum.value); }).
  attr("height", function(datum) { return y(datum.value); }).
  attr("width", barWidth).
  attr("fill", function(datum) { if (datum.value > 15) {return "blue";} else { return "yellow"; } });

barDemo.selectAll("text").
  data(awaydata).
  enter().
  append("svg:text").
  attr("x", function(datum, index) { return x(index) + barWidth; }).
  attr("y", function(datum) { return height - y(datum.value); }).
  attr("dx", -barWidth/2).
  attr("dy", "1.2em").
  attr("text-anchor", "middle").
  text(function(datum) { return datum.goals;}).
  attr("fill", "black");

var axisScale = d3.scale.linear()
                          .domain([0, 10])
                          .range([0, 600]);

//Create the Axis
var xAxis = d3.svg.axis()
                  .scale(axisScale)
                  .orient("bottom").ticks(10);

var xAxisGroup = barDemo.append("g")
.attr("class", "axis")
.attr("transform", "translate(0, 100)")
                              .call(xAxis);

var x = d3.scale.linear().domain([0, awaydata.length]).range([0, width]);
var y = d3.scale.linear().domain([0, d3.max(awaydata, function(datum) { return datum.value; })]).
  rangeRound([0, height]);

// add the canvas to the DOM
var barDemo = d3.select("#c2").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

barDemo.selectAll("rect").
  data(awaydata).
  enter().
  append("svg:rect").
  attr("x", function(datum, index) { return x(index); }).
  attr("y", function(datum) { return height - y(datum.value); }).
  attr("height", function(datum) { return y(datum.value); }).
  attr("width", barWidth).
  attr("fill", function(datum) { if (datum.value > 15) {return "blue";} else { return "yellow"; } });

barDemo.selectAll("text").
  data(awaydata).
  enter().
  append("svg:text").
  attr("x", function(datum, index) { return x(index) + barWidth; }).
  attr("y", function(datum) { return height - y(datum.value); }).
  attr("dx", -barWidth/2).
  attr("dy", "1.2em").
  attr("text-anchor", "middle").
  text(function(datum) { return datum.goals;}).
  attr("fill", "black");

var axisScale = d3.scale.linear()
                          .domain([0, 10])
                          .range([0, 600]);

//Create the Axis
var xAxis = d3.svg.axis()
                  .scale(axisScale)
                  .orient("bottom").ticks(10);

var xAxisGroup = barDemo.append("g")
.attr("class", "axis")
.attr("transform", "translate(0, 100)")
                              .call(xAxis);

var x = d3.scale.linear().domain([0, awaydata.length]).range([0, width]);
var y = d3.scale.linear().domain([0, d3.max(awaydata, function(datum) { return datum.value; })]).
  rangeRound([0, height]);

// add the canvas to the DOM
var barDemo = d3.select("#c4").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

barDemo.selectAll("rect").
  data(awaydata).
  enter().
  append("svg:rect").
  attr("x", function(datum, index) { return x(index); }).
  attr("y", function(datum) { return height - y(datum.value); }).
  attr("height", function(datum) { return y(datum.value); }).
  attr("width", barWidth).
  attr("fill", function(datum) { if (datum.value > 15) {return "blue";} else { return "yellow"; } });

barDemo.selectAll("text").
  data(awaydata).
  enter().
  append("svg:text").
  attr("x", function(datum, index) { return x(index) + barWidth; }).
  attr("y", function(datum) { return height - y(datum.value); }).
  attr("dx", -barWidth/2).
  attr("dy", "1.2em").
  attr("text-anchor", "middle").
  text(function(datum) { return datum.goals;}).
  attr("fill", "black");

var axisScale = d3.scale.linear()
                          .domain([0, 10])
                          .range([0, 600]);

//Create the Axis
var xAxis = d3.svg.axis()
                  .scale(axisScale)
                  .orient("bottom").ticks(10);

var xAxisGroup = barDemo.append("g")
.attr("class", "axis")
.attr("transform", "translate(0, 100)")
                              .call(xAxis);






}
