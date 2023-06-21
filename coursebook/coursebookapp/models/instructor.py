from django.db import models
from .app_user import AppUser

class Instructor(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to='instructors/', blank=True)

    def __str__(self):
        return self.last_name