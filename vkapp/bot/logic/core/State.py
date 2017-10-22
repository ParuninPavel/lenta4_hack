import logging as log


class State(object):

    def on_trigger(self, trigger):
        pass

    def _on_trigger(self, trigger):
        log.debug('== ' + str(self))
        return self.on_trigger(trigger)

    def on_enter(self, trigger):
        pass

    def _on_enter(self, trigger):
        log.debug('-> ' + str(self))
        return self.on_enter(trigger)

    def on_exit(self, trigger):
        pass

    def _on_exit(self, trigger):
        log.debug('<- ' + str(self))
        return self.on_exit(trigger)