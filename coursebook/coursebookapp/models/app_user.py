from django.db import models
from django.contrib.auth.models import User

# Password  - password
# Email  - email
# Firstname  - first_name
# Lastname  - last_name

# Company_name
# Phone_number


class AppUser(User):
    company_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15)
