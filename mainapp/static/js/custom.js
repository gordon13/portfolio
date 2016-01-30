// gallery info effect
$(".thumbnail").mouseenter( function (){

  	$(this).find(".dark-overlay, .info-overlay").show();

}).mouseleave( function (){

  	$(".dark-overlay, .info-overlay").hide();

}).on("click", function () {

	$fullscreen = $(".full-screen");
	$fullscreen.find(">img").remove();
	getFullSizeImage($fullscreen, $(this).data("url"));
	$fullscreen.show();

});

// full screen close button
$(".full-screen .close span, .full-screen img").on("click", function () {

	$fullscreen = $(".full-screen");
	$fullscreen.find(">img").remove();
	$fullscreen.hide();
	
});

function getFullSizeImage($target, url) {
	var image = $("<img />").attr('src', url)
    .on('load', function() {
        if (!this.complete || typeof this.naturalWidth == "undefined" || this.naturalWidth == 0) {
            console.log('broken image!');
        } else {
            $target.append(image);
        }
    });
}