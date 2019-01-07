from django.db import models

# Create your models here.
class ToDo(models.Model):
    item = models.CharField(max_length=100, primary_key=True)
