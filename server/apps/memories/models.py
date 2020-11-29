from django.db import models
from django.contrib.auth.models import User


class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memory')
    title = models.CharField(max_length=100)
    text = models.TextField()
    longitude = models.DecimalField(max_digits=23, decimal_places=16)
    latitude = models.DecimalField(max_digits=23, decimal_places=16)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s memory {self.title}"
