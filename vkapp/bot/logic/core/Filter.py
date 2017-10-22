import logging as log


class Filter(object):

    def __init__(self):
        pass

    def on_process(self, current_state, trigger):
        pass

    def _on_process(self, current_state, trigger):
        log.debug(':: ' + type(self).__name__)
        return self.on_process(current_state, trigger)