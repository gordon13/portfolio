// gallery thumbnail darkening effect
$(".thumbnail").mouseenter( function (){
  console.log("mouse in")
  $(".dark-overlay").show();
  $(this).find(".dark-overlay").hide();
  $(this).find(".info-overlay").show();
  timeoutObj.startT();
}).mouseleave( function (){
  console.log("mouse out");
  $(".dark-overlay").hide();
  $(".info-overlay").hide();
  timeoutObj.clearT();
});

function TimeoutObj(){
	var timeout = null;
	return {
	    startT: function(){
			timeout = setTimeout(function() {
		  		$(".dark-overlay").hide();
		  	}, 1000);
		},
		clearT: function(){
			clearTimeout(timeout);
		}
    }
}

var timeoutObj = TimeoutObj();