from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from .course import Course


class PurchasedCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} ({self.purchase_date})"
