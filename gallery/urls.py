from django.contrib import admin
from django.urls import path, include
from django.views.generic import *
from .models import Image

app_name = 'gallery'
urlpatterns = [
    path('', TemplateView.as_view(template_name='gallery/gallery_list.html'),name='list'),
    
    path('add/', CreateView.as_view(model=Image, fields='__all__')),
    
    path('list/', ListView.as_view(model=Image), name='image_list'),
    
    path('detail/<pk>/', DetailView.as_view(model=Image), name = 'image_detail')

]
