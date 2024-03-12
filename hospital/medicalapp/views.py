from django.shortcuts import render
from . import views

# Create your views here.


def medicalhome(req):
    return render(req, "medicalhome.html")
