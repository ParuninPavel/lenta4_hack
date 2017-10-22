from django.db import models


class VKUser(models.Model):
    vk_id = models.IntegerField(primary_key=True)


class Blogger(models.Model):
    id = models.AutoField(primary_key=True)
    vk_user = models.ForeignKey(VKUser, on_delete=models.CASCADE)
    balance = models.FloatField(null=False, default=0)


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    vk_user = models.ForeignKey(VKUser, on_delete=models.CASCADE)
