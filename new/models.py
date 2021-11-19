from django.db import models

# Create your models here.
class Token(models.Model):
    date=models.DateField(auto_now=True)