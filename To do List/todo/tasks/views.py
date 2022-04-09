from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

''' ROTA 1, PARA TESTE:
def index(request):
    return HttpResponse('Hello world')
'''

def index(request):
    #--- Informar isso somente item 22 em diante:
    tasks = Task.objects.all()
    form = TaskForm() #Informar isso após 24.1
    #--- Informar isso após 26
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    #---
    context = {'tasks':tasks, 'form':form} #Informar 'form' após 24.1
    #---
    return render(request, 'tasks/list.html', context) #Informar ', context' somente item 22 em diante

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'tasks/delete.html', context)