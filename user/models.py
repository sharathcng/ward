from django.db import models
from datetime import datetime,date
# Create your models here.

class RegisterModel(models.Model):
    name=models.CharField(max_length=300)
    userid=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    mobilenum=models.BigIntegerField()
    email=models.EmailField(max_length=400)
    gender=models.CharField(max_length=200)
    profile_pic=models.FileField()

class Post_Complaint(models.Model):
    user_id= models.ForeignKey(RegisterModel,on_delete=models.CASCADE,null=True,blank=True)
    category=models.CharField(max_length=2000)
    title=models.CharField(max_length=200)
    img=models.FileField()
    description=models.CharField(max_length=800)
    location=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now=True, auto_now_add=False)

class Notification(models.Model):
    N_title = models.CharField(max_length=200)
    N_img = models.FileField(null=True,blank=True)
    N_description = models.CharField(max_length=800)
    N_date = models.DateTimeField(auto_now=True, auto_now_add=False)


class ForwardedModel(models.Model):
    userd = models.BigIntegerField(max_length=50)
    category2=models.CharField(max_length=2000)
    title2=models.CharField(max_length=200)
    img2=models.FileField()
    description2=models.CharField(max_length=800)
    location2=models.CharField(max_length=500)
    date2=models.DateTimeField(auto_now=True, auto_now_add=False)