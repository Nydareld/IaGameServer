
var stage= new createjs.Stage("gameCanvas");
//var ws = new WebSocket("ws://127.0.0.1:5555/");
var tick=0;

var ip = "127.0.0.1"
var port = 5555

window.addEventListener('resize', resize, false);





 function resize() {
     stage.canvas.width = window.innerWidth-58;
     stage.canvas.height = window.innerHeight-140;
 }

function init() {

    resize();





    createjs.Ticker.setFPS(60);
    createjs.Ticker.addEventListener("tick", stage);


    $.ajax({
        type: "GET",
        url: "/data",
        dataType: "json",
        success: function(json) {
            $.each(json, function(key, val){
                for (j=0; j<val.length; j++){

                    var circle = new createjs.Shape();
                    circle.graphics.beginFill("DeepSkyBlue").drawCircle(0, 0, (val[j][1])*3);
                    circle.x = val[j][0][0]/10;
                    circle.y = val[j][0][1]/10;
                    stage.addChild(circle);
                }
            })
        }
    });

   stage.update();
    // this will show the info it in firebug console
}
