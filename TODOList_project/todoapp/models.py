from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()
    priority = models.IntegerField(choices=((1, 'Low'), (2, 'Medium'), (3, 'High')), default=1)
    completed=models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_datetime = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title


