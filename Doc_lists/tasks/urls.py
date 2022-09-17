from django.urls import path
from .views import ajoute_task, index,ajoute_collection
urlpatterns = [
    path('', index,name='home'),
    path('add/', ajoute_collection,name='name_views_add_collection'),
     path('add_task/', ajoute_task,name='name_views_add_task'),
 

]