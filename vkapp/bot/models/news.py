from django.db import models
from .users import Blogger, Admin


class News(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=300, blank=True, null=True)
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE, null=True)
    media = models.CharField(max_length=3000, blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)


class AdminReview(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    rating = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)


class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)


