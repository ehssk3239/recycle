from django.db import models
from django.utils import timezone

class User(models.Model):
    phone_number = models.CharField(primary_key=True, max_length=15)
    point = models.IntegerField(default=0)
    sum_points = models.IntegerField(default=0)
    # region_code = models.CharField(max_length=5)
