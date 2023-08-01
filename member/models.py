from django.db import models
# Create your models here.
class Member(models.Model):
    registerId = models.IntegerField()
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    course = models.CharField(max_length=255)
    CGPA = models.IntegerField()


