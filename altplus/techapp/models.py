from ast import increment_lineno
from calendar import TextCalendar
from django.db import models
from django.forms import PasswordInput

# Create your models here.
class WifiCreds(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    ssid = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=50)
    store_name = models.CharField(max_length=250, unique=True)
    schedule = models.TextField(max_length=250)

