// gallery info effect
$(".thumbnail").mouseenter( function (){

  	$(this).find(".dark-overlay, .info-overlay").show();

}).mouseleave( function (){

  	$(".dark-overlay, .info-overlay").hide();

}).on("click", function () {
	var modal_selector = ">.modal-dialog > .modal-content > .modal-body";
	var data = {"title":$(this).data("title"), "description":$(this).data("description")};
	console.log($(this))
	console.log(data)
	$fullscreen = $("#modal-full-screen");
	$modal = $fullscreen.find(modal_selector);
	$modal_image = $modal.find(">img");
	$modal_image.remove();
	makeModal($modal, $(this).data("url"), modal_selector+">img", data);
	$fullscreen.modal("show")
});

// full screen close button
$(".full-screen .close span, .full-screen img").on("click", function () {

	$fullscreen = $(".full-screen");
	$fullscreen.find(">img").remove();
	$fullscreen.hide();
	
});

function makeModal($target, url, image_selector, data) {
	$target.find(image_selector).attr("href", url);
	var image = $("<img />").attr('src', url)
    .on('load', function() {
        if (!this.complete || typeof this.naturalWidth == "undefined" || this.naturalWidth == 0) {
            console.log('broken image!');
        } else {
        	var $modal = $target.parent();

            var $link = $modal.find(".view-fullsize");
            $link.attr("href", url);

            var $title = $modal.find(".modal-title");
            $title.text(data.title)

            var $description = $modal.find(".modal-description");
            $description.text(data.description)

            $target.append(image);
        }
    });
}