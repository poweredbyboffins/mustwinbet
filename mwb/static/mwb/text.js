function text(winprob,loseprob,drawprob,id)
{
var w = 200;
var h = 200;
var r = h/2;
var color = d3.scale.category20().domain(d3.range(0,20));

var data = [{"label":"Home Win "+winprob+"%", "value":winprob}, 
		          {"label":"Away "+loseprob+"%", "value":loseprob}, 
		          {"label":"Draw "+drawprob+"%", "value":drawprob}];

var divname='#c'+id;
var ltext = "Home Win "+winprob+"%" +"Away Win"+loseprob+"%" +"Draw "+drawprob+"%";

return ltext;
}
