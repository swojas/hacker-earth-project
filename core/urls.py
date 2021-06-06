from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('input', views.SearchInput, name='input'),
    path('label', views.label, name='label')
]
