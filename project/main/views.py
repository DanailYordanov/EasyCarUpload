from .models import Model
from .forms import CarModelForm
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'main/home.html')


def create(request):

    if request.method == 'POST':
        form = CarModelForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            instance = form.save()
            return redirect(instance.get_absolute_url())
    else:
        form = CarModelForm()

    context = {
        'form': form
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
