from django.contrib.auth.models import User
from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=50)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name

class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)