from django.shortcuts import render

from app.models import *
# Create your views here.

def  topics(request):
    top=Topic.objects.all()
    d={'topics':top}
    return render(request,'topics.html',d)

def webpages(request):
    wop=Webpage.objects.all()
    d={'webpages':wop}
    return render(request,'webpages.html',d)

def accessrecord(request):
    aop=AccessRecord.objects.all()
    d={'access':aop}
    return render(request,'accessrecord.html',d)