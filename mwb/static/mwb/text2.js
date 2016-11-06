function text2(winprob,loseprob,drawprob,id)
{
var m = {top: 40, right: 45, bottom: 30, left: 40};
var w = 400;
var h = 30;
var r = h/2;
var color = d3.scale.category20().domain(d3.range(0,20));

var data = [{"label":"Home Win "+winprob+"%", "value":winprob}, 
		          {"label":"Away "+loseprob+"%", "value":loseprob}, 
		          {"label":"Draw "+drawprob+"%", "value":drawprob}];

var divname='#c'+id;
var ltext = "Home Win "+winprob+"%" +" Away Win "+loseprob+"%" +" Draw "+drawprob+"%";

var vis = d3.select(divname).append("svg:svg").data([data]).attr("width", w).attr("height", h).append("svg:g").attr("transform", "translate(" + r + "," + r + ")");

vis.append("text")
        .attr("x", 140)             
        .attr("y", 0 )
        .attr("text-anchor", "middle")  
        .style("font-size", "12px") 
        .text(ltext);

}
