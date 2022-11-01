from django.shortcuts import render, redirect
from .models import *

from .forms import *
# Create your views here.

def index(request):
    
    # querying the models
    tasks = Task.objects.all() 
    
    form = TaskForm() #the variable form is what is added to 'context'
    
    #receive the 'POST mthod from 'form' in 'list' template
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() #save the user inputs to our db
        return redirect('/') # keep the user on the same base url
    
    context = {'tasks': tasks, 'form': form} #dict context 'form' is from 'form = TaskForm'
    return render(request, 'list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk) #grabbing the task id from the url link
    
    form = TaskForm(instance=task) #we are passing the task grabbed above into the form
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    
    return render(request, 'task_update.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context = {'item': item}
    return render(request, 'delete.html', context)
