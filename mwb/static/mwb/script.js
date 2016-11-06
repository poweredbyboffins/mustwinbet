////////////////////////////////////////////////////////////
//////////////////////// Set-up ////////////////////////////
////////////////////////////////////////////////////////////

//Quick fix for resizing some things for mobile-ish viewers
var mobileScreen = ($( window ).innerWidth() < 500 ? true : false);

//Scatterplot
var margin = {left: 30, top: 20, right: 20, bottom: 20},
	width = Math.min($("#chart").width(), 800) - margin.left - margin.right,
	height = width*2/3;
			
var svg = d3.select("#chart").append("svg")
			.attr("width", (width + margin.left + margin.right))
			.attr("height", (height + margin.top + margin.bottom));
			
var wrapper = svg.append("g").attr("class", "chordWrapper")
			.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

//////////////////////////////////////////////////////
///////////// Initialize Axes & Scales ///////////////
//////////////////////////////////////////////////////

var opacityCircles = 0.7; 

//Set the color for each region
var color = d3.scale.ordinal()
					.range(["#EFB605", "#E58903", "#E01A25", "#C20049", "#991C71", "#66489F", "#2074A0", "#10A66E", "#7EB852"])
					.domain(["Africa | North & East", "Africa | South & West", "America | North & Central", "America | South", 
							 "Asia | East & Central", "Asia | South & West", "Europe | North & West", "Europe | South & East", "Oceania"]);
							 
//Set the new x axis range
var xScale = d3.scale.log()
	.range([0, width])
	.domain([100,2e5]); //I prefer this exact scale over the true range and then using "nice"
	//.domain(d3.extent(countries, function(d) { return d.GDP_perCapita; }))
	//.nice();
//Set new x-axis	
var xAxis = d3.svg.axis()
	.orient("bottom")
	.ticks(5)
	.scale(xScale);	
//Append the x-axis
wrapper.append("g")
	.attr("class", "x axis")
	.attr("transform", "translate(" + 0 + "," + height + ")")
	.call(xAxis);
		
//Set the new y axis range
var yScale = d3.scale.linear()
	.range([height,0])
	.domain(d3.extent(countries, function(d) { return d.lifeExpectancy; }))
	.nice();	
var yAxis = d3.svg.axis()
	.orient("left")
	.ticks(6)
	.scale(yScale);	
//Append the y-axis
wrapper.append("g")
		.attr("class", "y axis")
		.attr("transform", "translate(" + 0 + "," + 0 + ")")
		.call(yAxis);
		
//Scale for the bubble size
var rScale = d3.scale.sqrt()
			.range([mobileScreen ? 1 : 2, mobileScreen ? 10 : 16])
			.domain(d3.extent(countries, function(d) { return d.GDP; }));

		
////////////////////////////////////////////////////////////	
/////////////////// Scatterplot Circles ////////////////////
////////////////////////////////////////////////////////////	

//Initiate the voronoi group element	
var circleGroup = wrapper.append("g")
	.attr("class", "circleWrapper"); 
	
//Place the country circles	
wrapper.selectAll("countries")
	.data(countries.sort(function(a,b) { return b.GDP > a.GDP; })) //Sort so the biggest circles are below
	.enter().append("circle")
		.attr("class", "countries")
		.style("opacity", opacityCircles)
		.style("fill", function(d) {return color(d.Region);})
		.attr("cx", function(d) {return xScale(d.GDP_perCapita);})
		.attr("cy", function(d) {return yScale(d.lifeExpectancy);})
		.attr("r", function(d) {return rScale(d.GDP);})
		.on("mouseover", showTooltip)
		.on("mouseout", removeTooltip);

//////////////////////////////////////////////////////
///////////////// Initialize Labels //////////////////
//////////////////////////////////////////////////////

//Set up X axis label
wrapper.append("g")
	.append("text")
	.attr("class", "x title")
	.attr("text-anchor", "end")
	.style("font-size", (mobileScreen ? 8 : 12) + "px")
	.attr("transform", "translate(" + width + "," + (height - 10) + ")")
	.text("GDP per capita [US $] - Note the logarithmic scale");

//Set up y axis label
wrapper.append("g")
	.append("text")
	.attr("class", "y title")
	.attr("text-anchor", "end")
	.style("font-size", (mobileScreen ? 8 : 12) + "px")
	.attr("transform", "translate(18, 0) rotate(-90)")
	.text("Life expectancy");
	
///////////////////////////////////////////////////////////////////////////
///////////////////////// Create the Legend////////////////////////////////
///////////////////////////////////////////////////////////////////////////

if (!mobileScreen) {
	//Legend			
	var	legendMargin = {left: 5, top: 10, right: 5, bottom: 10},
		legendWidth = 160,
		legendHeight = 270;
		
	var svgLegend = d3.select("#legend").append("svg")
				.attr("width", (legendWidth + legendMargin.left + legendMargin.right))
				.attr("height", (legendHeight + legendMargin.top + legendMargin.bottom));			

	var legendWrapper = svgLegend.append("g").attr("class", "legendWrapper")
					.attr("transform", "translate(" + legendMargin.left + "," + legendMargin.top +")");
		
	var rectSize = 16, //dimensions of the colored square
		rowHeight = 22, //height of a row in the legend
		maxWidth = 125; //widht of each row
		  
	//Create container per rect/text pair  
	var legend = legendWrapper.selectAll('.legendSquare')  	
			  .data(color.range())                              
			  .enter().append('g')   
			  .attr('class', 'legendSquare') 
			  .attr("transform", function(d,i) { return "translate(" + 0 + "," + (i * rowHeight) + ")"; });
	 
	//Append small squares to Legend
	legend.append('rect')                                     
		  .attr('width', rectSize) 
		  .attr('height', rectSize) 			  		  
		  .style('fill', function(d) {return d;});                                 
	//Append text to Legend
	legend.append('text')                                     
		  .attr('transform', 'translate(' + 25 + ',' + (rectSize/2) + ')')
		  .attr("class", "legendText")
		  .style("font-size", "11px")
		  .attr("dy", ".35em")		  
		  .text(function(d,i) { return color.domain()[i]; });  
}//if !mobileScreen
else {
	d3.select("#legend").style("display","none");
}
	  
///////////////////////////////////////////////////////////////////////////
/////////////////// Hover functions of the circles ////////////////////////
///////////////////////////////////////////////////////////////////////////

//Hide the tooltip when the mouse moves away
function removeTooltip() {

	//Fade out the circle to normal opacity
	d3.select(this).style("opacity", opacityCircles);
	
	//Hide tooltip
	$('.popover').each(function() {
		$(this).remove();
	}); 

}//function removeTooltip

//Show the tooltip on the hovered over slice
function showTooltip(d) {
	
	//Define and show the tooltip
	$(this).popover({
		placement: 'auto top',
		container: '#chart',
		trigger: 'manual',
		html : true,
		content: function() { 
			return "<span style='font-size: 11px; text-align: center;'>" + d.Country + "</span>"; }
	});
	$(this).popover('show');

	//Make chosen circle more visible
	d3.select(this).style("opacity", 1);
					
}//function showTooltip

//iFrame handler
var pymChild = new pym.Child();
pymChild.sendHeight()
setTimeout(function() { pymChild.sendHeight(); },5000);

