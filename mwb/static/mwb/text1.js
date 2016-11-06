function text1(ltext,id)
{
var m = {top: 40, right: 45, bottom: 30, left: 40};
var w = 400;
var h = 25;
var r = h/2;
var color = d3.scale.category20().domain(d3.range(0,20));


var divname='#c'+id;

var vis = d3.select(divname).append("svg:svg").attr("width", w).attr("height", h).append("svg:g").attr("transform", "translate(" + r + "," + r + ")");

vis.append("text")
        .attr("x", 140)             
        .attr("y", 0 )
        .attr("text-anchor", "middle")  
        .style("font-weight",900)
        .style("font-size", "14px") 
        .text(ltext);

}
