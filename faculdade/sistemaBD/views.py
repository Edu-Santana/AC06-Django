from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'sistemaBD/index.html')

#{% load staticfiles %}
#<link href="{% static "css/estilo.css" %}" rel="stylesheet">
