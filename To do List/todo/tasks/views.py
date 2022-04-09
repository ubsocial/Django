from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

'''
ROTA 1, PARA TESTE:
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