


$(document).ready(function() {
  

   

         
		
		
		$("#bouton").click(function () {
       var character  = $("#txt").val();
        
    

        history.pushState('data', '', "/"+character);
       
    });

  //   history.pushState(null, null, character );
  		

       $(".nav a").on("click", function(){
            $(".nav").find(".active").removeClass("active");
            $(this).parent().addClass("active");

        


    });

    





});



