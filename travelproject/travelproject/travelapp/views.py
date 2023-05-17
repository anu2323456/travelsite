from django.shortcuts import render
from django.http import HttpResponse

from .models import Place
from .models import Teams

def about(request):
    obj=Place.objects.all()
    obj1 =Teams.objects.all()
    return render(request,"index.html",{'result':obj,'result1': obj1})



