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
    date=models.DateTimeField(auto_now_add=True)