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
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Форма була не коректною'


    form  = TaskForm()
    context={
        'form': form,
        'error': error
    }
    return render(request,'menv/create.html',context)

