$(function () {

    // Add box-shadow to the navbar

    $(window).scroll(function () {
        var pos = $(window).scrollTop();
        if (pos > 1) {
            $("header").addClass('sticky');
        }
        else {
            $("header").removeClass('sticky');
        }
    });

});