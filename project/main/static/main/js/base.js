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

    // // Submit uploaded images

    // $('#id_images').change(submitFormAjax);

    // function submitFormAjax() {
    //     var form = $('#createForm')[0];
    //     var formData = new FormData(form);

    //     $.ajax({
    //         type: 'POST',
    //         url: $(form).attr('action'),
    //         data: formData,
    //         cache: false,
    //         contentType: false,
    //         processData: false,
    //         success: function (data) {
    //             $('#id_images').val('');
    //         },
    //         error: function (data) {
    //             alert('Нещо се обърка. Опитайте отново!');
    //         }
    //     });
    // }

    // Upload files

    var formData = new FormData();

    $('#id_images').change(uploadFiles);

    function uploadFiles() {
        var fileData = $('#id_images').prop('files');

        for (var i = 0; i < fileData.length; i++) {
            formData.append('images', fileData[i]);
        }

        loadImages(formData.getAll('images'));
        console.log(formData.getAll('images').length);

    };

    function loadImages(files) {
        for (var i = 0; i < files.length; i++) {
            readURL(files[i]);
        }
    };

    function readURL(file) {
        var reader = new FileReader();

        reader.onload = function (e) {
            var input = $('.input-image[src=""]').first();
            input.attr('src', e.target.result);
            input.attr('name', file['name']);
        };

        reader.readAsDataURL(file);
    }

    $('#delete').click(removeImage);

    function removeImage(name) {
        name = 'koli 5 229.jpg';
        for (var i = 0; i < formData.getAll('images').length; i++) {
            if (formData.getAll('images')[i].name == name) {
                formData.getAll('images').splice(i);
                console.log(formData.getAll('images'));
            }
        }
        console.log(formData.getAll('images'));
    };

});