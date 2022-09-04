from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50)
    symptoms = models.TextField(null=True, blank=True)
    help = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "courses"


class Message(models.Model):
    content = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

