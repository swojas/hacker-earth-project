from django.shortcuts import render
from django.http import request
from django.template.response import TemplateResponse
from core.models import DataBase
# Create your views here.


def index(request):
    return render(request, 'index.html')


def SearchInput(request):
    if request.method == 'POST':
        searchQuery = request.POST.get('search', None)
        args = {}
        args['search'] = searchQuery
        return TemplateResponse(request, "index.html", args)


def label(request):
    if request.method == 'POST':
        input1 = request.POST.get('id1', None)
        input2 = request.POST.get('id2', None)
        instance = DataBase(input1=input1, input2=input2)
        instance.save()
        return render(request, "index.html")
