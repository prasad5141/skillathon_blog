from django.db import models
# from django.contrib.auth import User

from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False, blank=False)


class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=5000)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, blank=True)


