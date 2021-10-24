from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Model, Image
from .forms import CarModelForm, IMAGES_NUMBER


def home(request):
    return render(request, 'main/home.html')


@login_required
def create(request):
    if request.method == 'POST' and request.is_ajax():
        form = CarModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = request.user
            instance = form.save()

            for image in request.FILES.getlist('images'):
                Image.objects.create(car=instance, image=image)

        else:
            return JsonResponse(form.errors)
    else:
        form = CarModelForm()

    context = {
        'form': form,
        'images_number_list': range(IMAGES_NUMBER)
    }

    return render(request, 'main/create.html', context)


def load_models(request):
    brand_id = request.GET.get('brand_id')

    if brand_id != '':
        models = Model.objects.filter(brand=brand_id)
    else:
        models = Model.objects.none()

    context = {
        'models': models
    }

    return render(request, 'main/models_dropdown_options.html', context)
