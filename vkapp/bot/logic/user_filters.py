from .core.Filter import Filter
from .utils import stickers
from .user_states import StatisticsState, ProposeNewsState, AdminChatState


class StatsFilter(Filter):
    def on_process(self, current_state, trigger):
        sticker_result = stickers.is_sticker(trigger.get_update())

        if sticker_result[0]:
            if sticker_result[1] == '4193':
                return StatisticsState()


class ProposeNewsFilter(Filter):
    def on_process(self, current_state, trigger):
        sticker_result = stickers.is_sticker(trigger.get_update())

        if sticker_result[0]:
            if sticker_result[1] == '2920':
                return ProposeNewsState()


class AdminChatFilter(Filter):
    def on_process(self, current_state, trigger):
        sticker_result = stickers.is_sticker(trigger.get_update())

        if sticker_result[0]:
            if sticker_result[1] == '4650':
                return AdminChatState()
