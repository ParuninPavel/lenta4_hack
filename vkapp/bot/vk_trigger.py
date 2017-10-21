import vk
import os
from vk.exceptions import VkAPIError
from functools import wraps

#
# def try_api(func):
#     @wraps(func)
#     def wrap(*args, **kwargs):
#         attempts = 3
#         while attempts > 0:
#             try:
#                 func(*args, **kwargs)
#                 attempts = 0
#             except VkAPIError:
#                 session = vk.Session(access_token=os.environ['GROUP_TOKEN'])
#                 VKTrigger.vkapi = vk.API(session)
#                 attempts -= 1


class VKTrigger:
    session = vk.Session(access_token=os.environ['GROUP_TOKEN'])
    vkapi = vk.API(session)

    @classmethod
    def _use_api(cls, *args, **kwargs):
        attempts = 3
        while attempts > 0:
            try:
                cls.vkapi(*args, **kwargs)
                attempts = 0
            except VkAPIError as error:
                attempts -= 1
                if attempts <= 0:
                    raise error
                session = vk.Session(access_token=os.environ['GROUP_TOKEN'])
                cls.vkapi = vk.API(session)
                attempts -= 1

    @classmethod
    def send_message(cls, uid, text):
        #VKTrigger.vkapi('messages.send', user_id=uid, message=text)
        cls._use_api('messages.send', user_id=uid, message=text)

