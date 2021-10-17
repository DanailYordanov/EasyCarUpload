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

    // Submit uploaded images

    $('#id_images').change(uploadFiles);

    $('#delete').click(removeImage);

    $('form').submit(function (e) {
        submitForm(e);
    });

});

function modelOptionsLoad() {
    var brand_id = $(this).val();
    var loadModelsUrl = $('#createForm').attr('data-models-url');

    $.ajax({
        url: loadModelsUrl,
        data: {
            'brand_id': brand_id
        },
        success: function (data) {
            $('#id_model').html(data);
            $('#id_model').niceSelect('update');
        },
        error: function (response) {
            alert('Нещо се обърка. Опитайте отново!');
        }
    });
}

var uploadedImages = [];

function uploadFiles() {
    var fileData = $('#id_images').prop('files');

    for (let i = 0; i < fileData.length; i++) {
        uploadedImages.push(fileData[i]);
    }

    loadImages(fileData);

    $('#id_images').val('');
};

function loadImages(files) {
    for (var i = 0; i < files.length; i++) {
        readURL(files[i]);
    }
};

function readURL(file) {
    var reader = new FileReader();

    reader.onload = function (e) {
        var inputedImage = $('.inputed-image[src=""]').first();
        inputedImage.attr('src', e.target.result);

        var parentDiv = inputedImage.parent();
        parentDiv.show();
        parentDiv.next().hide();
    };

    reader.readAsDataURL(file);
}

function removeImage(parentImgContainer) {
    var inputedImage = parentImgContainer.find('.inputed-image');
    var imageNumber = inputedImage.attr('image-number');

    uploadedImages.splice(imageNumber, 1);

    clearImages();
    loadImages(uploadedImages);
};

function clearImages() {
    $('div.single-image-wrapper').hide();
    $('.inputed-image').attr('src', '');
    $('label.single-image-wrapper').show();
}

function submitForm(e) {
    e.preventDefault();

    var form = $(this);
    var url = form.attr('action');
    var csrf_token = $("input[name=csrfmiddlewaretoken]").val();
    var formData = new FormData($('form')[0]);
    uploadedImages.forEach(image => formData.append('images', image));

    $.ajax({
        url: url,
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        headers: {
            'X-CSRFToken': csrf_token
        },
        success: function (response) {
            $('.errorlist').empty();
            for (error in response) {
                $('[name="' + error + '"]').parent().find('.errorlist').html('<li>' + response[error] + '</li>');
            };
        },
    });
}