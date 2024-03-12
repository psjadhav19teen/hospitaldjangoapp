from django.shortcuts import render


# Create your views here.
def pathologyhome(req):
    return render(req, "pathologyhome.html")
