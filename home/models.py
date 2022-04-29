from distutils.command.upload import upload
from django.db import models
import os
def filepath(request,filename):
    return os.path.join('uploads/',filename)
# Create your models here.
class Task(models.Model):
    taskTitle=models.CharField(max_length=30)
    taskDesc=models.TextField()
    taskImage=models.ImageField(null=True,blank=True,upload_to=filepath)
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.taskTitle