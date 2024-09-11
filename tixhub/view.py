from django.shortcuts import render
from base.models import Movies

def home(req):
    return render(req, "index.html")

def info(req):
    MovieData = Movies.objects.get()

    data = {
        'MovieData' : MovieData
    }

    return render(req, "info.html", data)
