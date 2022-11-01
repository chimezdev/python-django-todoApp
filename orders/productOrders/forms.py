from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm): #name your model
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    # 'title' above is the name of the attr in the models.py file.
    class Meta:
        model = Task    #def which model you want to create a form for
        fields = ("__all__") #def fields we want to allow in the form, here we allow all
    