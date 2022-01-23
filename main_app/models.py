from django.db import models

# Create your models here.
class Widget(models.Model): #add class of Widgets, with form model.
    description = models.CharField(max_length=50)  #project requirement
    quantity = models.IntegerField()            #project requirement

    def __str__(self):  #represents the class's objects as string
        return self.item    #return the instance created.


