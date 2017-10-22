from django.conf.urls import url

from . import views

# api_url=https://api.vk.com/api.php
# &api_settings=0
# &viewer_id=123456
# &group_id=654321
# &is_app_user=0 

urlpatterns = [
    url(
        regex=r'^auth/',
        view=views.init,
        name='auth'
    ),
    url(
        regex=r'^blogers/',
        view=views.blogers,
        name='blogers'
    ),
    url(
        regex=r'^news/',
        view=views.blogers,
        name='news'
    ),
    url(
        regex=r'^news1/',
        view=views.blogers,
        name='news1'
    ),
    url(
        regex=r'^news2/',
        view=views.blogers,
        name='news2'
    ),
]
