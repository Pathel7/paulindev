from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content_post = models.TextField()
    author_post = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)


class Com(models.Model):
    content_com = models.TextField()
    date_com = models.DateTimeField(auto_now_add=True)
    author_com = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mes = models.TextField()


