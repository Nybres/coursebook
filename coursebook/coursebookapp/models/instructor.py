from django.db import models
from .app_user import AppUser


class Instructor(models.Model):
    app_user = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, related_name="instructors_created"
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to="instructors/", blank=True)

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname
