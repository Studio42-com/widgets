from django.urls import path #this is for below, path equating to what how we identify it is a path
from . import views
# from .models import WidgetForm

urlpatterns = [
    path('', views.index, name='index'), #this will be the path to new index page
    path('addnewwidget',views.addnewwidget, name='addnewwidget'), #not an actual link
        #this is a "virtual" location to pass through to save the form submission
        path('delete/<int:item>', views.fastDelete, name='fast_delete'),
    ]