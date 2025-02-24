from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser) : 
    phone_number = models.CharField(max_length=11 , unique=True)

class Category(models.Model)  :
    name = models.CharField(max_length=255,unique= True)
class Tasks(models.Model): 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    descriptions = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    user_task_id = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:  
            last_task = Tasks.objects.filter(user=self.user).order_by('-user_task_id').first()
            self.user_task_id = (last_task.user_task_id + 1) if last_task else 1
        super().save(*args, **kwargs)
