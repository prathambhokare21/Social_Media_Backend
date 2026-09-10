from django.db import models
from django.conf import settings
# Create your models here.
 
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_posts", blank=True)
    image = models.ImageField(upload_to= "posts/", null=True, blank=True)

    def  __str__(self):
        return self.user.username
