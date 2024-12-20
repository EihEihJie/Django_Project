from django.db import models

# Create your models here.
#1.自己定义模型
# class User(models.Model):
#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=20, unique=True)
#     email = models.EmailField(unique=True)
#2.django自带一个用户模型
# 这个用户模型
# 有密码加密和密码验证
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True)
    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name