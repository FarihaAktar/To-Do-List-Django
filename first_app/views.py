from django.shortcuts import render, redirect
from first_app.forms import TaskForm
from first_app.models import TaskModel

# Create your views here.

def home(request):
    return render(request, 'add_tasks.html')


def add_Task(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            # print(task.cleaned_data)
            return redirect('show_tasks')
    else:
        task = TaskForm()
    
    return render(request, 'add_tasks.html', {'form': task})


def show_tasks(request):
    tasks = TaskModel.objects.all()
    # print(tasks)
    return render(request, 'show_tasks.html', {'data': tasks})


def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    return render(request, 'add_tasks.html', {'form': form})

def delete_task(request, id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect(request.META['HTTP_REFERER'])
    # return redirect('show_tasks')

def complete_task(request, id):
    task = TaskModel.objects.get(pk = id)
    task.is_completed = True
    task.save()
    return redirect('completed_tasks')

def completed_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'completed_tasks.html', {'data': tasks})
