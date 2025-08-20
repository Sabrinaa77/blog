from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  published = models.BooleanField(default=True)
