"""orders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="list"),
    path('task_update/<str:pk>/', views.updateTask, name="task_update"), #the <str:pk> will append the task id to the url when submited. we can also have <int:pk>
    path('delete/<str:pk>/', views.deleteTask, name="delete") #the <str:pk> will append the task id to the url when submited. we can also have <int:pk>
    
]