// gallery thumbnail darkening effect
$(".thumbnail").mouseenter( function (){
  console.log("mouse in")
  $(".overlay").show();
  $(this).find(".overlay").hide();
}).mouseleave( function (){
  console.log("mouse out");
  $(".overlay").hide();
});
