from django.db import models
from datetime import date

# Create your models here.

class Task(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDis = models.TextField()
    taskTime = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle