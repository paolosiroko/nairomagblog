from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
            User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=20, null=False)
    published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=False, blank=False)
    brief = models.TextField(max_length=50 , default="")

    description = models.TextField()

    def __str__(self):
        return self.title