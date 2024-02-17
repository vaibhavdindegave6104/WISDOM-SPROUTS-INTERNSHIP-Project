
"""
URL configuration for TODOList_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from todoapp import views

urlpatterns = [
    path('home/',views.homeview,name="home"),
    path('home1/',views.home_view,name="home_view"),
    path('task_info/',views.task_info,name="task_info"),
    path('login/',views.login_view,name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('register/',views.register_view,name="register"),
    path('add_task/',views.add_task,name="add_task"),
    path('update/<int:id>',views.update_task,name="update"),
    path('delete/<int:id>/',views.delete_task, name='delete'),
   # path('send/<int:id>/',views.sendemail,name='send')
]

