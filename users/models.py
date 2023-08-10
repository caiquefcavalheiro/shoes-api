from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=False, null=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=40)
    birthdate = models.DateField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
