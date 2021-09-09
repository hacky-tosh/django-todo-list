from django.contrib import admin
from django.urls import path, include
from todolistapp import views


urlpatterns = [
    path('',views.home,name='home'),
    path('task',views.task,name='task'),
    path('delete-task/<int:id>',views.deletet,name='delete')
]
