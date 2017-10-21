import json
from .vk_trigger import VKTrigger

def handle_update(update):
    uid = update[3]
    print(update, uid)
    VKTrigger.send_message(uid, str(uid))
