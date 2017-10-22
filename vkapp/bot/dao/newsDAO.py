from vkapp.bot.models import Blogger, News, AdminReview, Publication
from .usersDAO import get_or_create_blogger
from datetime import datetime, timedelta, time


def new_news(link, media, uid, pic):
    blogger = get_or_create_blogger(uid)
    news = News(link=link, blogger=blogger, media=media, pic=pic)
    news.save()
    return news

def get_news_proposed_today(uid):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())

    news = News.objects.filter(blogger__vk_user__vk_id=uid).filter(date_time__lte=today_end,
                                                                   date_time__gte=today_start)
    return news

def news_by_blogger(uid):
    blogger = get_or_create_blogger(uid)
    news = News.objects.filter(blogger=blogger)
    return news

def get_news_review_rating(news):
    review = AdminReview.objects.filter(news=news)
    if len(review)==0:
        return 0
    else:
        return review[0].rating

def is_news_published(news):
    published_info = Publication.objects.filter(news=news)
    if len(published_info) == 0:
        return False
    else:
        return True
