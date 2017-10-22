from .core.State import State
import time
from .utils.stickers import is_sticker
from vkapp.bot.dao import usersDAO, newsDAO

class BootStrapState(State):
    def on_trigger(self, trigger):
        usersDAO.new_blogger(trigger.current_uid)

        trigger.send_message(trigger.current_uid,
                             message='Привет! Я умный бот для Лентача, разработанный компанией Cleverbots')

        trigger.send_message(trigger.current_uid, message='https://cleverbots.ru')
        time.sleep(3)


        trigger.send_message(trigger.current_uid,
                             message='Тут ты сможешь предлагать новости и получать за них деньги!')
        time.sleep(3)

        trigger.send_message(trigger.current_uid, message='Держи набор стикеров!')
        time.sleep(3)

        trigger.send_message(trigger.current_uid, message='<набор стикеров тут>')
        time.sleep(3)

        trigger.send_message(trigger.current_uid, message='Это секретные стикеры, с их помощью ты сможешь управлять мной!')
        time.sleep(3)



        trigger.send_message(trigger.current_uid, message='Чтобы предложить новость, отправь мне стикер "Поехали"')
        time.sleep(1.5)
        trigger.send_message(trigger.current_uid, sticker_id=2920)
        time.sleep(3)

        trigger.send_message(trigger.current_uid, message='Чтобы связаться с администратором Лентача, отправь мне стикер "Я Вам пишу"')
        time.sleep(1.5)
        trigger.send_message(trigger.current_uid, sticker_id=4650)
        time.sleep(3)

        trigger.send_message(trigger.current_uid, message='Чтобы просмотреть статистику по своим новостям и по балансу, '
                                                          'а также вывести деньги, отправь мне стикер "Расскажи-ка"')
        time.sleep(1.5)
        trigger.send_message(trigger.current_uid, sticker_id=4193)

        time.sleep(3)
        trigger.send_message(trigger.current_uid,
                             message='Ну что, начнем? 😉')
        return RootState()


class RootState(State):
    def on_enter(self, trigger):
        trigger.get_user_struct().erase_queue()
        pass

    def on_trigger(self, trigger):
        update = trigger.get_update()
        trigger.send_message(trigger.current_uid,
                             message=is_sticker(update))

        sticker_result = is_sticker(update)

        if sticker_result[0]:
            if sticker_result[1]=='2920':
                return ProposeNewsState()
            else:
                trigger.send_message(trigger.current_uid,
                                     message='Неопознанный стикер!')
        else:
            trigger.send_message(trigger.current_uid, message='Неопознанное сообщение!')

class ProposeNewsState(State):
    def on_enter(self, trigger):
        trigger.send_message(trigger.current_uid,
                             message='Отлично! Пиши сюда все, что нужно. Как закончишь, отправь мне стикер "Огонь"')

        trigger.send_message(trigger.current_uid, sticker_id=3007)

    def on_trigger(self, trigger):
        update = trigger.get_update()
        sticker_result = is_sticker(update)

        if sticker_result[0]:
            if sticker_result[1]=='3007':
                return RootState()

    def on_exit(self, trigger):
        media_news = trigger.get_user_struct().message_queue[1:-1]
        news = newsDAO.new_news(None, media_news, trigger.current_uid)
        trigger.send_message(trigger.current_uid, message='Ок, новость сохранена. Ее просмотрят администраторы, и ты получишь '
                                                          'уведомление о статусе ее рассмотрения')

