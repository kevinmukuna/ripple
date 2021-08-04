// Create sliders and galleries

$(document).ready(function() {

    var sliders = $('.gallery');

    // Create a slider and gallery for each post
    sliders.each(function(){
        var slider = $(this).lightSlider({
            gallery:true,
            item:1,
            thumbItem:5,
            slideMargin: 0,
            speed:500,
            pause: 3000,
            auto:true,
            loop:true,
            onSliderLoad: function() {
                $('.gallery').removeClass('cS-hidden');
            }     
        });
    });

    // Classify all PostImage depending on the size for styling
    var imgs = $('.gallery li img');
    imgs.each(function(){
        var img = $(this);
        var width = img.width();
        var height = img.height();
        if(width < height){
            img.addClass('portrait');
        }else{
            img.addClass('landscape');
        }
    });
});