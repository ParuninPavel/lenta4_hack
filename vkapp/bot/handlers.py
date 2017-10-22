from vkapp.bot.logic.core.vk_trigger import VKTrigger
from .logic.core.StateMachine import StateMachine
from multiprocessing import Process, Array

def handle_update(update):
    uid = update[3]

    state_machine = StateMachine()
    # p = Process(target=state_machine.fire, args=(VKTrigger, uid, update))
    # p.start()
    state_machine.fire(VKTrigger, uid, update)

