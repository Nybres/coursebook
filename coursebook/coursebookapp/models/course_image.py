from typing import Iterable, Optional
from django.db import models
from django.utils.text import slugify
from .course import Course
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage


class CourseImage(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def get_upload_path(instance, filename):
        course_slug = slugify(instance.course.title)
        # return "course_images/{}/{}".format(course_slug, filename)
        return f"course_images/{course_slug}/{filename}"

    image = models.ImageField(upload_to=get_upload_path)

    def __str__(self):
        return self.course.title
    
@receiver(pre_delete, sender=CourseImage)
def course_pre_delete(sender, instance, **kwargs):
    if instance.image:
        default_storage.delete(instance.image.path)
