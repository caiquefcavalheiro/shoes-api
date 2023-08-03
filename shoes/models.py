from django.db import models


class Shoes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    image = models.CharField(max_length=255)
    description = models.TextField()
