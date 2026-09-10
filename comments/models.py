from django.db import models
from django.conf import settings
from posts.models import Post
# Create your models here.

class Comments(models.Model):
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)