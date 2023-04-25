from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    about=models.TextField(blank=True)
    image=models.ImageField(blank=True,null=True)

class Address(models.Model):
    address_type=models.CharField(max_length=10)
    phone=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE) # one to many

class Product(models.Model):
    p_name=models.CharField(max_length=30)
    category=models.CharField(max_length=10)
    user=models.ManyToManyField(User)


# class Branch(models.Model):
#     branch_name=models.TextField
#     branch_id=models.IntegerField

# class Teacher(models.Model):
#     teacher_id=models.IntegerField
#     first_name=models.CharField(max_length=30)
#     last_name=models.CharField(max_length=30)
#     branch=models.OneToOneField(Branch,on_delete=models.)

