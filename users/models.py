from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):
    username = None
    email = None
    phone = models.CharField(max_length=16, unique=True)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name']