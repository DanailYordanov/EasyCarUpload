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

});

var formData = new FormData();

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

function uploadFiles() {
    var fileData = $('#id_images').prop('files');

    for (var i = 0; i < fileData.length; i++) {
        formData.append('images[]', fileData[i]);
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
        inputedImage.attr('image-name', file['name']);

        var parentDiv = inputedImage.parent();
        parentDiv.show();
        parentDiv.next().hide();
    };

    reader.readAsDataURL(file);
}

function removeImage(parentImgContainer) {
    var inputedImage = parentImgContainer.find('.inputed-image');
    var imageName = inputedImage.attr('image-name');
    var filtered = formData.getAll('images[]').filter(image => image['name'] != imageName);

    formData.delete('images[]');
    filtered.forEach(image => formData.append('images[]', image));

    clearImages();
    loadImages(formData.getAll('images[]'));
};

function clearImages() {
    $('div.single-image-wrapper').hide();
    $('.inputed-image').attr('image-name', '');
    $('.inputed-image').attr('src', '');
    $('label.single-image-wrapper').show();
}