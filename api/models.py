from django.db import models
from django.utils import timezone


# Create your models here.

class Task(models.Model):
   
   
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='task_images/', max_length=255, null=True, blank=True)
    audio = models.FileField(upload_to='audio/', max_length=255, null=True, blank=True)

   

    def __str__(self):
        return self.title

 