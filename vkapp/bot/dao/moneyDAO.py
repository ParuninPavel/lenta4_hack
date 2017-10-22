from vkapp.bot.models import Income, Payment, Blogger, News
from .usersDAO import get_or_create_blogger

def new_income_proposal(amount, news):
    income = Income(amount=amount, news=news, type=Income.PROPOSAL)
    blogger = news.blogger
    blogger.balance += amount
    blogger.save()
    income.save()

def re_count_balance(uid):
    blogger = get_or_create_blogger(uid)

    incomes = Income.objects.filter(news__blogger__vk_user__vk_id=uid).select_related()

    new_balance = 0
    for value in incomes:
        new_balance += value.amount

    payments = Payment.objects.filter(blogger=blogger)
    for value in payments:
        new_balance -= value.amount

    blogger.balance = new_balance
    blogger.save()

    return new_balance



