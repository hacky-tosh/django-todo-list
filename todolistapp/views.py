from django.shortcuts import render, HttpResponse
from todolistapp.models import Task
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        title = request.POST.get('task')
        desc = request.POST.get('dis')
        ins = Task(taskTitle=title, taskDis=desc)
        ins.save()
        messages.success(request,'Task has been added :)')


    return render(request, 'index.html')

def task(request):
    allTask = Task.objects.all()
    context = {'tasks':allTask}

    return render(request, 'task.html',context)
