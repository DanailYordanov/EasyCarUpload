from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def create(request):
    return render(request, 'main/create.html')
