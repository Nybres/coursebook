from django.db import models
from .instructor import Instructor

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    province_choices = (
        ('dolnośląskie', 'Dolnośląskie'),
        ('kujawsko-pomorskie', 'Kujawsko-Pomorskie'),
        ('lubelskie', 'Lubelskie'),
        ('lubuskie', 'Lubuskie'),
        ('łódzkie', 'Łódzkie'),
        ('małopolskie', 'Małopolskie'),
        ('mazowieckie', 'Mazowieckie'),
        ('opolskie', 'Opolskie'),
        ('podkarpackie', 'Podkarpackie'),
        ('podlaskie', 'Podlaskie'),
        ('pomorskie', 'Pomorskie'),
        ('śląskie', 'Śląskie'),
        ('świętokrzyskie', 'Świętokrzyskie'),
        ('warmińsko-mazurskie', 'Warmińsko-Mazurskie'),
        ('wielkopolskie', 'Wielkopolskie'),
        ('zachodniopomorskie', 'Zachodniopomorskie'),
    )
    province = models.CharField(max_length=30, choices=province_choices)
    available = models.BooleanField(default=False)
    short_description = models.CharField(max_length=200)
    seats = models.PositiveIntegerField()
    date = models.DateField()
    city = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.title