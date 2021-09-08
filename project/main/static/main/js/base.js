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

    // Load model dropdown options

    $('#id_brand').change(modelOptionsLoad);

    function modelOptionsLoad() {
        var brand_id = $(this).val();
        var loadModelsUrl = $("#createForm").attr("data-models-url")

        $.ajax({
            url: loadModelsUrl,
            data: {
                'brand_id': brand_id
            },
            success: function (data) {
                $("#id_model").html(data);
                $('#id_model').niceSelect('update');
            },
            error: function (response) {
                alert('Нещо се обърка. Опитайте отново!')
            }
        });
    }
});