from django.shortcuts import render, redirect
from .models import WidgetForm
from django.views.generic.edit import CreateView
# from .forms import Widget_Form
# from django.shortcuts import HttpResponse

# Create your views here.
def index(request): # This brings up the view to the homepage
    widgets = WidgetForm.objects.all()
    return render(request, 'index.html', {'widgets': widgets})    #notice index.html

class WidgetList(CreateView):   #formView
    model = WidgetForm
    fields = "__all__"
    success_url = "/"

def addnewwidget(request):
    mywidget = WidgetForm(description=request.POST['description'],quantity=request.POST['quantity'])
    mywidget.save()
    return redirect('/')

#using an immediate delete
def fastDelete(request, item):
    widget = WidgetForm.objects.get(pk=item)
    widget.delete()
    return redirect('/')

