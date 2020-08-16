from django.db import models

# Create your models here.
class Guest(models.Model):
    first_name = models.TextField(max_length=120)
    last_name = models.TextField(max_length=120)
    phone_number = models.IntegerField()
    active = models.BooleanField(default=True)
