from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks=Task.objects.order_by('-id')
    return render(request,'menv/index.html',{'title':'Головна сторінка сайту','tasks':tasks})


def about(request):
    return render(request,'menv/about.html')

def create(request):
    error=''
    thx=''
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            thx='Дякую за ваш запит! \nМи вам зателефонуємо😁'
        else:
            error='Форма була не коректною!'


    form  = TaskForm()
    context={
        'form': form,
        'error': error,
        'thx':thx
    }
    return render(request,'menv/create.html',context)

