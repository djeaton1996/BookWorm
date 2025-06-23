from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_genre = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"