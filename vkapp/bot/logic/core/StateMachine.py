# -*- coding: utf-8 -*-
from vkapp.bot.logic.user_filters import StatsFilter, ProposeNewsFilter, AdminChatFilter

class StateMachine(object):
    def __init__(self):
        self.state = None
        self.user_struct = None
        self.filters = [StatsFilter(), ProposeNewsFilter(), AdminChatFilter()]

    def fire(self, trigger, uid, update):
        # trigger.user = self.user
        trigger.current_uid = uid
        self.user_struct = trigger.queue_machine.get_user_struct(uid)
        self.state = self.user_struct.state

        self.user_struct.push(update)

        print('STATE=',self.state)

        for f in self.filters:
            filtered_state = f._on_process(self.state, trigger)
            if filtered_state:
                self.to_state(filtered_state, trigger)
                trigger.queue_machine.get_user_struct(uid).state = self.state
                return

        new_state = self.state._on_trigger(trigger)
        self.to_state(new_state, trigger)
        trigger.queue_machine.get_user_struct(uid).state = self.state

    def to_state(self, new_state, trigger):
        if not new_state:
            return self.state

        if new_state == self.state:
            reenter_state = self.state._on_enter(trigger)
            self.to_state(reenter_state, trigger)
            return

        exit_state = self.state._on_exit(trigger)
        if exit_state:
            self.to_state(exit_state, trigger)
            return

        self.state = new_state

        enter_state = self.state._on_enter(trigger)
        if enter_state:
            self.to_state(enter_state, trigger)
            return

#global_state_machine = StateMachine()


