from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):

    name = models.CharField("Name", max_length=120)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
