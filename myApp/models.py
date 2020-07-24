from django.db import models

# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)


class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE, )

# from django.contrib.auth.models import AbstractUser
# class UserProfile(AbstractUser):
#     mobile=models.CharField(max_length=11,verbose_name='手机号码',unique=True)
#     icon=models.ImageField(upload_to='uploads/%Y/%m/%d')

from captcha.fields import CaptchaField
class blogUser(models.Model):
    username=models.CharField(max_length=32,unique=True)
    userpassword = models.CharField(max_length=50, unique=True)
    useremail= models.CharField(max_length=60, unique=True)
    usericon= models.ImageField(upload_to='icons/%Y/%m/%d')
    is_active=models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    captcha = CaptchaField()
    # objects = models.Manager()
    # class Meta:
    #     db_table='blog_user'
