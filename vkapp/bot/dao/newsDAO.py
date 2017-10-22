from vkapp.bot.models import Blogger, News
from .usersDAO import get_or_create_blogger

def new_news(link, media, uid):
    blogger = get_or_create_blogger(uid)
    news = News(link=link, blogger=blogger, media=media)
    news.save()
    return news
