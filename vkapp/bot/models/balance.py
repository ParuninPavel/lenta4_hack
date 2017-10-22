from django.db import models
from .users import Blogger, VKUser
from .news import News


class Income(models.Model):
    PROPOSAL = 'PROP'
    CANCEL = 'PUB'
    INCOME_CHOICES = (
        (PROPOSAL, 'Предложение новости'),
        (CANCEL, 'Опубликование новости'))

    id = models.AutoField(primary_key=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    type = models.CharField(max_length=4, choices=INCOME_CHOICES, default=PROPOSAL)
    amount = models.FloatField(null=False, default=0)
    date_time = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    payer = models.ForeignKey(VKUser, on_delete=models.CASCADE)
    mount = models.FloatField(null=False, default=0)
    date_time = models.DateTimeField(auto_now_add=True)
