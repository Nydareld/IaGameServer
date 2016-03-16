
// var stage= new createjs.Stage("gameCanvas");
//var ws = new WebSocket("ws://127.0.0.1:5555/");
var tick=0;

var ip = "127.0.0.1"
var port = 5555

window.addEventListener('resize', resize, false);

var svg = d3.select("#gameCanvas").append("svg")
    .attr("width", window.innerWidth-58)
    .attr("height", window.innerHeight-140);



function resize() {
    $("#gameCanvas").width(window.innerWidth-58);         //Largeur
    $("#gameCanvas").height(window.innerHeight-140);      //Hauteur
    // console.log("Zbra");
 }


function init() {

    resize();
    //
    // createjs.Ticker.setFPS(60);
    // createjs.Ticker.addEventListener("tick", stage);

    var colors = new Array();

    setInterval(function(){
        resize();


        $.ajax({
            type: "GET",
            url: "/data",
            dataType: "json",
            success: function(json) {
                var data = Array();
                var max = 0;
                $.each(json, function(key, val){
                    if( colors[key] == null ){
                        colors[key] = '#'+(0x1000000+(Math.random())*0xffffff).toString(16).substr(1,6);
                    }
                    for (j=0; j<val.length; j++){

                        size = Math.sqrt(val[j][1]);
                        if(size>max){
                            max = size;
                        }
                        x = val[j][0][0]/10000*(window.innerWidth-58);
                        y = val[j][0][1]/10000*(window.innerHeight-140);
                        data.push({
                            "x":x,
                            "y":y,
                            "r":size,
                            "color":colors[key],
                            "name":""
                        });

                    }
                    // console.log(key.concat("=".concat(max)));
                })
                console.log(max);

                d3.selectAll("svg > *").remove();

                var nodes = svg.selectAll(".node")
                    .data(data)
                    .enter()
                    .append("g")
                    .attr("class","node")
                    .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });


                nodes.append("circle")
                    .attr("r", function(d) {return d.r})
                    .style("fill",function(d){return d.color;})

                nodes.append("text")
                    .attr("dy", ".3em")
                    .style("text-anchor", "middle")
                    .text(function(d) { return d.name; });
            }
        });

     }, 30);


    // this will show the info it in firebug console
}
