function pienew(winprob,loseprob,drawprob,homeform,awayform,pctwin,pctaway,id)
{
var m = {top: 40, right: 45, bottom: 30, left: 40};
var w = 200;
var h = 200;
var r = h/2;
var color = d3.scale.category20().domain(d3.range(0,20));

winprob=Math.round(winprob);
loseprob=Math.round(loseprob);
drawprob=Math.round(drawprob);

var data = [{"label":"H "+winprob+"%", "value":winprob}, 
		          {"label":"L "+loseprob+"%", "value":loseprob}, 
		          {"label":"D "+drawprob+"%", "value":drawprob}];

var divname='#c'+id;
var ltext = "Home Win "+winprob+"%" +"Away Win"+loseprob+"%" +"Draw "+drawprob+"%";

var vis = d3.select(divname).append("svg:svg").data([data]).attr("width", w).attr("height", h).append("svg:g").attr("transform", "translate(" + r + "," + r + ")");

var pie = d3.layout.pie().value(function(d){return d.value;});

// declare an arc generator function
var arc = d3.svg.arc().outerRadius(r);

// select paths, use arc generator to draw
var arcs = vis.selectAll("g.slice").data(pie).enter().append("svg:g").attr("class", "slice");
arcs.append("svg:path")
    .attr("fill", function(d, i){
        j=Math.floor(Math.random() * 20) + 1
        return color(j);
    })
    .attr("d", function (d) {
        // log the result of the arc generator to show how cool it is :)
        console.log(arc(d));
        return arc(d);
    });

// add the text
arcs.append("svg:text").attr("transform", function(d){
			d.innerRadius = 0;
			d.outerRadius = r;
    return "translate(" + arc.centroid(d) + ")";})
                        .attr("text-anchor", "end").text( function(d, i) {
    return data[i].label;})
    .style("font-size","9px");

}
