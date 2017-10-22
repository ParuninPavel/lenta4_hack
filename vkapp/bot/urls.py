# from .polling import get_polling_server, polling
from django.conf.urls import url
# from multiprocessing import Process
from .handlers import handle_update

# p = Process(target=polling)
# p.start()
urlpatterns = [
    url(r'^$', handle_update, name='index')
]
