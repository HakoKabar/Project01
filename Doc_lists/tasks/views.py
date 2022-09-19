from gc import get_objects
from glob import escape
from inspect import CO_ASYNC_GENERATOR
from tracemalloc import take_snapshot
from typing import Collection

from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Collection, Task
from django.utils.text import slugify


def index(request):
    context={}
   
    collection_slug=request.GET.get("co")
    
    if collection_slug :
        collection=get_object_or_404(Collection,slug=collection_slug)
    
    
    context['collectt']=Collection.objects.order_by('slug')
    context["affiche"]=collection.task_set.order_by('description')
    
    
   
 
   
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