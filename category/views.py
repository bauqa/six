
from django.shortcuts import render, redirect

from category.forms import TaskForm
from .models import Task
# Create your views here.

def index(req):
    tasks = Task.objects.all()
    return render(req,'main/index.html',{'title': 'Home',
                                        'tasks': tasks})

def about(req):
    return render(req,'main/about.html')

def add(req):

    if req.method == 'POST':
        
        form = TaskForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'ERROR_$)$'

    form = TaskForm()

    context = {
        'form':form
    }
    return render(req,'main/products.html',context)