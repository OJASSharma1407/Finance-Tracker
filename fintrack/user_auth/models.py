from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reg_user(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.email
