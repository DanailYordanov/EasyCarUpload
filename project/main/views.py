from .models import Model
from .forms import CarModelForm, MAX_IMAGE_FORMS_NUM
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'main/home.html')


@login_required
def create(request):
    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES)
        if request.is_ajax():
            pass
    else:
        form = CarModelForm()

    blank_forms_num = range(MAX_IMAGE_FORMS_NUM)
    context = {
        'form': form,
        'blank_forms_num': blank_forms_num
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
