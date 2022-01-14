from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    roles =models.ManyToManyField(to='Role')

    def __str__(self):
        return self.name


class Role(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Permission(models.Model):
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=128)
    roles = models.ManyToManyField(to='Role')
    action = models.CharField(max_length=16, default='')  # 设置一下默认值，免得报错
    group = models.ForeignKey(to='PermissionGroup', default='1', on_delete=models.CASCADE)  # 设置一下默认值，免得报错


    def __str__(self):
        return self.title


class PermissionGroup(models.Model):
    title = models.CharField(max_length=32,)  # 设置一下默认值，免得报错

    def __str__(self):
        return self.title
