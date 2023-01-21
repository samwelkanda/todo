"""todos_app URL Configuration

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

from todos.views import todos, add_todo, delete_todo, edit_todo, mark_done

urlpatterns = [
    path('', todos, name='todos'),
    path('add-todo/', add_todo, name='add_todo'),
    path('mark-done/<int:pk>/', mark_done, name='mark_done'),
    path('delete/<int:pk>/', delete_todo, name='delete_todo'),
    path('edit/<int:pk>/', edit_todo, name='edit_todo'),
    path('admin/', admin.site.urls),
]
