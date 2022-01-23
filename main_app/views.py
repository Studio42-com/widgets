from django.shortcuts import render
from .models import Widget

# Create your views here.
def index(request): # This brings up the view to the homepage
    return render(request, 'index.html')    #notice index.html

