
var stage= new createjs.Stage("gameCanvas");
//var ws = new WebSocket("ws://127.0.0.1:5555/");
var tick=0;

var ip = "127.0.0.1"
var port = 5555

window.addEventListener('resize', resize, false);



function tick(){
    tick++;

    $.ajax({
        url : "http://".concat(ip).concat(":").concat(port),
        type : "get",
        datatype: "json",
        success: function(data){
            console.log(data[0]);
        },
    })

    console.log(tick);
    stage.update();
}

 function resize() {
     stage.canvas.width = window.innerWidth-58;
     stage.canvas.height = window.innerHeight-140;
 }

function init() {

    resize();
     var circle = new createjs.Shape();
     circle.graphics.beginFill("DeepSkyBlue").drawCircle(0, 0, 50);
     circle.x = 100;
     circle.y = 100;
     stage.addChild(circle);

    createjs.Tween.get(circle, { loop: true })
  .to({ x: 400 }, 1000, createjs.Ease.getPowInOut(4))
  .to({ alpha: 0, y: 175 }, 500, createjs.Ease.getPowInOut(2))
  .to({ alpha: 0, y: 225 }, 100)
  .to({ alpha: 1, y: 200 }, 500, createjs.Ease.getPowInOut(2))
  .to({ x: 100 }, 800, createjs.Ease.getPowInOut(2));
  stage.update();

  $.ajax({
      url : "http://".concat(ip).concat(":").concat(port),
      type : "jsonp",
      datatype: "json",
      success: function(data){
          console.log(data[0]);
      },
  })

    createjs.Ticker.setFPS(60);
    createjs.Ticker.addEventListener("tick", stage);
}
