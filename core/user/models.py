from django.db import models

# Create your models here.



#user model
class user(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(max_length=10)
    