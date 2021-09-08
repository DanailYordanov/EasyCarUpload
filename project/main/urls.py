from . import views
from django.urls import path

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('load-models/', views.load_models, name='load-models')
]
