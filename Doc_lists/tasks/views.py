from glob import escape
from typing import Collection
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Collection, Task

def index(request):
    context={}
    collectt=Collection.get_defaut_collection()
    context['collectt']=Collection.objects.order_by('name')
   
    return render(request,'home.html',context=context)
   

def ajoute_collection(request):
    coll_name = escape(request.POST.get("input_collection-name"))
    coll,created=Collection.objects.get_or_create(name=coll_name)
    if not created :
        return HttpResponse(' la collection  ** {} **existe deja'.format(coll.name))
    return redirect("home")

def ajoute_task(request):
    collect=Collection.get_defaut_collection()
    descri=escape(request.POST.get("input_add_description"))
    Task.objects.create(description=descri, collection=collect)
    return redirect("home")