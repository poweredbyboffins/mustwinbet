function quad(winprob,awayprob,drawprob,homeform,awayform,pctwin,pctaway,id)
{
var divname='#c'+id;
var color = d3.scale.category20().domain(d3.range(0,20));

var width = 480,
    height = 480,
    dotRadius = 4,
    gridSpacing = 10;

var svg = d3.select(divname).append("svg")
    .attr("width",width)
    .attr("height",height);

//Scales for item positions
var x = d3.scale.linear().domain([-10,10]).range([0,width]);
var y = d3.scale.linear().domain([-10,10]).range([height,0]);

//gridlines
svg.append("path")
  .attr("class","grid")
  .attr("d",function() {
    var d = "";

    for (var i = gridSpacing; i < width; i += gridSpacing ) {
      d += "M"+i+",0 L"+i+","+height;
    }

    for (var i = gridSpacing; i < height; i += gridSpacing ) {
      d += "M0,"+i+" L"+width+","+i;
    }

    return d;
  })

//x axis
svg.append("path")
  .attr("class","axis")
  .attr("d","M0,"+height/2+" L"+width+","+height/2);

//y axis
svg.append("path")
  .attr("class","axis")
  .attr("d","M"+width/2+",0 L"+width/2+","+height);

//Data - x and y can be anything positive or negative
//Domains for scales need to be wide enough.
//Currently -10 to +10
var itemList = [
  {
    x: 5,
    y: 5,
    description: "I'm in the upper-right quadrant!"
  },
  {
    x: -5,
    y: -5,
    description: "I'm in the lower-left quadrant!"
  }
];

var dataprob = [
{ d : winprob, t : "Home Win " }
, {d: awayprob, t: "Away Win " }
, { d: drawprob,t:"Draw Prob " }
];
var dataform = [
 { d:homeform,t:"Home Form " }
, {d:awayform,t:"Away Form "}
, {d:pctwin,t:"Pct Win "}
, {d:pctaway,t:"Pct Away Win "}
];
  

//One group per item
var items = svg.selectAll("g.item").data(itemList).enter().append("g")
  .attr("class","item");

var starty=115;
var startx=242;
var textpos;
var wdth;

for (var i=0; i < dataprob.length; i++)  
{
starty=starty+25;
wdth=dataprob[i].d;
if (dataprob[i].d < 0){
startx=242-dataprob[i].d*-1;
wdth=dataprob[i].d*-1;
}
else { startx=242 ; }
items.append("rect")
  .attr("x",startx)
  .attr("y",starty)
  .attr("rx",5)
  .attr("ry",5)
  .attr("width",wdth)
  .attr("height",20)
  .style("fill", function(d, i){
        j=Math.floor(Math.random() * 20) + 1
        return color(j);
    })
  ;
textpos=starty+10;
items.append("text")
  .attr("x",342)
  .attr("y",textpos)
  .text(dataprob[i].t+dataprob[i].d+"%");
}
var starty=115;
var startx=0;

for (var i=0; i < dataform.length; i++)  
{
starty=starty+25;
wdth=dataform[i].d;
if (dataform[i].d < 0){
startx=0+dataform[i].d*-1;
wdth=dataform[i].d*-1;
}
else { startx=0 ; }
items.append("rect")
  .attr("x",startx)
  .attr("y",starty)
  .attr("rx",5)
  .attr("ry",5)
  .attr("width",wdth)
  .attr("height",20)
  .style("fill", function(d, i){
        j=Math.floor(Math.random() * 20) + 1
        return color(j);
    })
  ;
textpos=starty+10;
items.append("text")
  .attr("x",100)
  .attr("y",textpos)
  .text(dataform[i].t+dataform[i].d+"%");
//Add a label
//would need to use .getBBox() to make sure this doesn't hit the sides
/*items.append("text")
  .attr("x",function(d){
    return x(d.x);
  })
  .attr("y",function(d){
    return y(d.y);
  })
  .attr("dy","1.25em")
  .attr("text-anchor","middle")
  .text(function(d){return d.description;});
*/
}

}
