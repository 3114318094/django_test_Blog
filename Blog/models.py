from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name='blog_posts',on_delete=models.CASCADE)
    body = models.TextField()
    publish_time = models.DateTimeField(default=timezone.now)
    modifies_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish_time',)

    def __str__(self):
        return self.title
