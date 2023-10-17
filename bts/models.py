from django.db import models

# Create your models here.
class bhagtan(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    age = models.IntegerField()
    singer = models.CharField(max_length=25)


