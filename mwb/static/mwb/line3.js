function line(home,away,id)

{
var w = 400;
var h = 200;
var r = h/2;
var color = d3.scale.category20().domain(d3.range(0,20));

var divname='#c'+id;

 
 var data = [{
"sale": "202",
"year": "200"
}, {
"sale": "215",
"year": "202"
}, {
"sale": "179",
"year": "204"
}, {
"sale": "199",
"year": "206"
}, {
"sale": "134",
"year": "208"
}, {
"sale": "176",
"year": "210"
}];

var data2 = [{
"sale": "152",
"year": "200"
}, {
"sale": "189",
"year": "202"
}, {
"sale": "179",
"year": "204"
}, {
"sale": "199",
"year": "206"
}, {
"sale": "134",
"year": "208"
}, {
"sale": "176",
"year": "210"
}];

var vis = d3.select(divname).append("svg:svg").attr("width",w).attr("height",h),
WIDTH = 400,
HEIGHT = 200,
MARGINS = {
top: 20,
right: 20,
bottom: 20,
left: 50
},
xScale = d3.scale.linear().range([MARGINS.left, WIDTH - MARGINS.right]).domain([200, 210]),
yScale = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([134, 215]),
xAxis = d3.svg.axis()
.scale(xScale),
yAxis = d3.svg.axis()
.scale(yScale)
.orient("left");

vis.append("g")
.attr("class", "x axis")
.attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
.call(xAxis);

vis.append("g")
.attr("class", "y axis")
.attr("transform", "translate(" + (MARGINS.left) + ",0)")
.call(yAxis);

var lineGen = d3.svg.line()
.x(function(d) {
return xScale(d.year);
})
.y(function(d) {
return yScale(d.sale);
})
.interpolate("basis");

vis.append('svg:path')
.attr('d', lineGen(data))
.attr('stroke', 'green')
.attr('stroke-width', 2)
.attr('fill', 'none');

vis.append('svg:path')
.attr('d', lineGen(data2))
.attr('stroke', 'blue')
.attr('stroke-width', 2)
.attr('fill', 'none');

}

