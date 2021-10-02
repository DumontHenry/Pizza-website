from django.shortcuts import render
from .models import Pizza
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def index(request):
    pizzas = Pizza.objects.all().order_by('prix')
    context = {'pizza': pizzas}
    return render(request, "menu/index.html", context)

def api_get_pizzas(request):
    pizzas = Pizza.objects.all().order_by('prix')
    json = serializers.serialize('json', pizzas)
    return HttpResponse(json)