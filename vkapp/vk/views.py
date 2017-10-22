from django.shortcuts import render

# def init(request, api_url, api_settings, viewer_id, group_id, is_app_user):
#     return render(request, 'vk/index.html', context)

# api_url=https://api.vk.com/api.php
# &api_settings=0
# &viewer_id=123456
# &group_id=654321
# &is_app_user=0 \\
from django.views.decorators.clickjacking import xframe_options_exempt
from vkapp.bot.dao.newsDAO import get_news_proposed_today
from vkapp.bot.models import Blogger, News, AdminReview, Publication
from datetime import datetime, timedelta, time

@xframe_options_exempt
def init(request, **request_params):
    param = list(request.GET.items()) #.get('viewer_id')
    news_cnt = News.objects.filter(date_time__lte=today_end, date_time__gte=today_start).count()
    return render(request, 'vk/index.html', {'news_count': news_cnt})
    # context = {'data': param}
    # return render(request, 'vk/index.html', context)

@xframe_options_exempt
def blogers(request):
    return render(request, 'vk/news.html', {'news': news})

@xframe_options_exempt
def news(request):
    return render(request, 'vk/news1.html', {'news': news})

@xframe_options_exempt
def news1(request):
    return render(request, 'vk/news2.html', {'news': news})

@xframe_options_exempt
def news2(request):
    return render(request, 'vk/news.html', {'news': news})

@xframe_options_exempt
def like(request, news_id):
    news = News.objects.filter(id=news_id)
    review = AdminReview.objects.get(news=news)
    review.rating = 1
    review.save()
    return render(request, 'vk/init.html')

@xframe_options_exempt
def dislike(request, news_id):
    news = News.objects.filter(id=news_id)
    review = AdminReview.objects.get(news=news)
    review.rating = -1
    review.save()
    return render(request, 'vk/init.html')