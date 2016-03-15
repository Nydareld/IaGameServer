
var stage= new createjs.Stage("gameCanvas");
//var ws = new WebSocket("ws://127.0.0.1:5555/");
var tick=0;

var ip = "127.0.0.1"
var ort = 5555

window.addEventListener('resize', resize, false);



function tick(){
    tick++;
    stage.update();
}

 function resize() {
     stage.canvas.width = window.innerWidth-58;
     stage.canvas.height = window.innerHeight-140;
 }

function init() {

    resize();
    // var circle = new createjs.Shape();
    // circle.graphics.beginFill("DeepSkyBlue").drawCircle(0, 0, 50);
    // circle.x = 100;
    // circle.y = 100;
    // stage.addChild(circle);
    stage.update();
    createjs.Ticker.setFPS(60);
    createjs.Ticker.addEventListener("tick", stage);
}
