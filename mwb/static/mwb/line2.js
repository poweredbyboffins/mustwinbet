function line2(home,away,id)
{
var w = 200;
var h = 200;
var r = h/2;
var color = d3.scale.category20().domain(d3.range(0,20));

var divname='#fc'+id;

 
 var barData = [{
    'x': 1,
    'y': home
  }, {
    'x': 2,
    'y': away
  }];

  var formatAxis = d3.format("c");

  var vis = d3.select(divname).append("svg:svg").attr("wdith",w).attr("height",h).append("svg:g"),
    WIDTH = 300,
    HEIGHT = 200,
    MARGINS = {
      top: 20,
      right: 20,
      bottom: 20,
      left: 50
    },
    xRange = d3.scale.ordinal().rangeRoundBands([MARGINS.left, WIDTH - MARGINS.right], 0.1).domain(barData.map(function (d) {
      return d.x;
    })),


/*      .tickFormat(function(d) { return datalabel[d].label; }) */


    yRange = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([-100,100]),

    xAxis = d3.svg.axis()
      .scale(xRange)
      .ticks(2)
      .tickFormat(function(d) { if (d==1) return "Home Form"; if (d==2) return "Away Form"; }) 
      .orient("bottom");


    yAxis = d3.svg.axis()
      .scale(yRange)
      .ticks(3)
      .orient("left")
      .tickSubdivide(true);


  vis.append('svg:g')
    .attr('class', 'x axis')
    .attr('transform', 'translate(0,' + (HEIGHT - MARGINS.bottom) + ')')
    .style("font-size","10px")
    .call(xAxis);

  vis.append('svg:g')
    .attr('class', 'y axis')
    .attr('transform', 'translate(' + (MARGINS.left) + ',0)')
    .call(yAxis);

  vis.selectAll('rect')
    .data(barData)
    .enter()
    .append('rect')
    .attr('x', function (d) {
      return xRange(d.x);
    })
    .attr('y', function (d) {
      return yRange(d.y);
    })
    .attr('width', xRange.rangeBand())
    .attr('height', function (d) {
      return ((HEIGHT - MARGINS.bottom) - yRange(d.y));
    })
    .attr('fill', function(d, i){
        j=Math.floor(Math.random() * 20) + 1
        return color(j);
    })
}

