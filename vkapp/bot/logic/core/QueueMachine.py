from enum import Enum
from vkapp.bot.logic.user_states import BootStrapState, RootState

# class UserStates(Enum):
#     news_proposing = 1
#     chat_with_admin = 2
#     statistics_mode = 3
#     undefined = 0

class UserStruct:
    def __init__(self):
        self.message_queue=[]
        self.state=BootStrapState()
        #self.state = RootState()

    def push(self, update):
        self.message_queue.append(update)

    def pop(self):
        update = None
        if len(self.message_queue)>0:
            update = self.message_queue[0]
            self.message_queue = self.message_queue[1:]
        return update

    def erase_queue(self):
        self.message_queue = []

    def get_last_update(self):
        update = None
        if len(self.message_queue) > 0:
            update = self.message_queue[-1]
        return update



class QueueMachine:
    def __init__(self):
        self.users_cache = {}

    def get_user_struct(self, user_id):
        if user_id in self.users_cache:
            return self.users_cache[user_id]
        else:
            struct = UserStruct()
            self.users_cache[user_id] = struct
            return struct

