from django.urls import path #this is for below, path equating to what how we identify it is a path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #this will be the path to new index page
]