
from django.conf import settings
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import time
from .form import TaskForm, UserRegisterForm, UserLoginForm
from .models import Task
from datetime import datetime, timedelta
from django.core.mail import send_mail
import schedule
import pytz

def homeview(request):
    return render(request,'todoapp/home.html')
def home_view(request):
    return render(request,'todoapp/home1.html')

def task_info(request):

    print(request.user)  # Add this line for debugging
    tasks_with_user = Task.objects.filter(user=request.user).select_related('user').order_by('priority')
    return render(request, 'todoapp/task_info.html', {'tasks_with_user':tasks_with_user})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_info')

    form = TaskForm()
    return render(request, 'todoapp/add_task.html', {'form': form})


def update_task(request,id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_info')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todoapp/update_task.html', {'form': form, 'task': task})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_info')
    return render(request, 'todoapp/delete_task.html', {'task': task})

def login_view(request):
    if request.method=="POST":
        loginform=UserLoginForm(data=request.POST)
        if loginform.is_valid():
            user = loginform.get_user()
            login(request, user)
            # Redirect to a specific page after login
            return redirect('task_info')

    loginform = UserLoginForm()
    return render(request, 'todoapp/login.html', {'form': loginform})
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'todoapp/register.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirect to a specific page after logout (e.g., home page)
    return redirect('home')

"""
def sendemail(request,id):
    tasks_with_user  = get_object_or_404(Task, id=id, user=request.user)
    notification_time = tasks_with_user.due_datetime - timedelta(minutes=5)
    print(tasks_with_user.due_datetime)
    print("N=",notification_time)
  #  newtime=datetime.time().strftime("%H:%M",notification_time)
    print("D=",datetime.now())
    formatted_notification_time = notification_time.strftime('%H:%M:%S')
    print("Formatted Notification Time:", formatted_notification_time)
    current_time = timezone.now()
    print("Current Time:", current_time)
    formatted_notification_datetime = timezone.make_aware(datetime.strptime(formatted_notification_time, '%H:%M:%S'), timezone=pytz.utc)
    print("Formatted notification datetime", formatted_notification_datetime )


    if current_time <= formatted_notification_datetime :
        print("In if")
        schedule.every().day.at('formatted_notification_time').do(send_mail('Task Reminder',
                  'Dear {}, Task is starting in {} minutes.'.format(id,tasks_with_user.due_datetime),
                  settings.EMAIL_HOST_USER,
        ['parudkarkomal@gmail.com']
        ))
    else:
        print("In else")

    return redirect('home')
"""
"""
    if datetime.now() == notification_time:
        send_mail('Task Reminder',
                  'Dear {}, Task is starting in {} minutes.'.format(id,tasks_with_user.due_datetime),
                  settings.EMAIL_HOST_USER,
        ['parudkarkomal@gmail.com']
        )"""

