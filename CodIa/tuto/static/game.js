
var stage= new createjs.Stage("gameCanvas");
//var ws = new WebSocket("ws://127.0.0.1:5555/");
var tick=0;

var ip = "127.0.0.1"
var port = 5555

window.addEventListener('resize', resize, false);





 function resize() {
     stage.canvas.width = window.innerWidth-58;         //Largeur
     stage.canvas.height = window.innerHeight-140;      //Hauteur
 }


function init() {

    resize();

    createjs.Ticker.setFPS(60);
    createjs.Ticker.addEventListener("tick", stage);

    setInterval(function(){

        stage.removeAllChildren();

        $.ajax({
            type: "GET",
            url: "/data",
            dataType: "json",
            success: function(json) {
                $.each(json, function(key, val){
                    var max = 0;
                    var color = '#'+(0x1000000+(Math.random())*0xffffff).toString(16).substr(1,6);
                    for (j=0; j<val.length; j++){

                        var circle = new createjs.Shape();

                        var size = Math.sqrt(val[j][1]);
                        if(size/10>max){
                            max = size/10;
                        }
                        circle.graphics.beginFill(color).drawCircle(0, 0, size/10);
                        circle.x = val[j][0][0]/10000*stage.canvas.width;
                        circle.y = val[j][0][1]/10000*stage.canvas.height;
                        stage.addChild(circle);
                    }
                    console.log(key.concat("=".concat(max)));
                })
            }
        });

        stage.update();

    }, 10);

    // this will show the info it in firebug console
}
