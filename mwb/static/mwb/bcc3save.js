function bcc(id,datafile)
{
/*var color = d3.scale.category10().domain(d3.range(0,20));*/

var canvas = document.querySelector(id),
    context = canvas.getContext("2d");

var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = canvas.width - margin.left - margin.right,
    height = canvas.height - margin.top - margin.bottom;

var x = d3.scaleBand()
    .rangeRound([0, width])
    .padding(0.1);

var y = d3.scaleLinear()
    .rangeRound([height, 0]);

context.translate(margin.left, margin.top);

/*data.forEach(function(d) {
  d.date = parseDate(d.date);
  d.close = +d.close;
}
);
*/

d3.requestTsv(datafile, function(d) {
  d.fthg = +d.fthg;
  return d;
}, function(error, data) {
  if (error) throw error;

  x.domain(data.map(function(d) { return d.hometeam; }));
  y.domain([0, d3.max(data, function(d) { return d.fthg; })]);

  var yTickCount = 10,
      yTicks = y.ticks(yTickCount),
      yTickFormat = y.tickFormat(yTickCount, "0f");


  context.beginPath();
  x.domain().forEach(function(d) {
    context.moveTo(x(d) + x.bandwidth() / 2, height);
    context.lineTo(x(d) + x.bandwidth() / 2, height + 6);
  });
  context.strokeStyle = "black";
  context.stroke();

  context.textAlign = "center";
  context.textBaseline = "top";
  x.domain().forEach(function(d) {
    context.fillText(d, x(d) + x.bandwidth() / 2, height + 6);
  });

  context.beginPath();
  yTicks.forEach(function(d) {
    context.moveTo(0, y(d) + 0.5);
    context.lineTo(-6, y(d) + 0.5);
  });
  context.strokeStyle = "black";
  context.stroke();

  context.textAlign = "right";
  context.textBaseline = "middle";
  yTicks.forEach(function(d) {
    context.fillText(yTickFormat(d), -9, y(d));
  });

  context.beginPath();
  context.moveTo(-6.5, 0 + 0.5);
  context.lineTo(0.5, 0 + 0.5);
  context.lineTo(0.5, height + 0.5);
  context.lineTo(-6.5, height + 0.5);
  context.strokeStyle = "black";
  context.stroke();

  context.save();
  context.rotate(-Math.PI / 2);
  context.textAlign = "right";
  context.textBaseline = "top";
  context.font = "bold 10px sans-serif";
  context.fillText("Frequency", -10, 10);
  context.restore();

  var num=770;
  data.forEach(function(d) {
    context.fillRect(x(d.hometeam), y(d.fthg), x.bandwidth(), height - y(d.fthg));
    num=num+7;
    txt = num.toString();
    context.fillStyle="#"+txt;
  });
 //canvas.toDataURL("image/png");  // here is the most important part because if you dont replace you will get a DOM 18 exception.
//window.open(image); // it will save locally
});

}
