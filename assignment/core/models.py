from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    email = models.EmailField(max_length=40, unique=True)
    phone = models.CharField(max_length=12, null= True, blank=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
