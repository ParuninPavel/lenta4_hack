import vk
import os
from vk.exceptions import VkAPIError
from functools import wraps
from .QueueMachine import QueueMachine

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
    queue_machine = QueueMachine()
    session = vk.Session(access_token=os.environ['GROUP_TOKEN'])
    vkapi = vk.API(session)
    current_uid=None

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
    def send_message(cls, uid, **kwargs):
        #VKTrigger.vkapi('messages.send', user_id=uid, message=text)
        cls._use_api('messages.send', user_id=uid, **kwargs)

    @classmethod
    def get_update(cls):
        uid = cls.current_uid
        user_struct = cls.queue_machine.get_user_struct(uid)
        return user_struct.get_last_update()

    @classmethod
    def get_user_struct(cls):
        uid = cls.current_uid
        user_struct = cls.queue_machine.get_user_struct(uid)
        return user_struct

