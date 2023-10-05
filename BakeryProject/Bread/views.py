from django.shortcuts import render
from .models import Bread 

def index(request, size=-1): 
    if size in [10,15,20,25,30,40,50,100]:
        breads = Bread.objects.filter(size=size)
    else:
        breads = Bread.objects.all()
    count = breads.count()
    return render(request, "Bread/home.html", {"count": count, "breads": breads})

