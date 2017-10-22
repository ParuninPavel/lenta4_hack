from .core.State import State
import time
from .utils.stickers import is_sticker
from vkapp.bot.dao import usersDAO, newsDAO, moneyDAO
import json

PROPOSAL_AMOUNT=1
PUBLISH_AMOUNT=100
MAX_DAILY_NEWS=10

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
            elif sticker_result[1] == '4193':
                return StatisticsState()
            elif sticker_result[1] == '4650':
                return AdminChatState()
            else:
                trigger.send_message(trigger.current_uid,
                                     message='Неопознанный стикер!')
        else:
            trigger.send_message(trigger.current_uid, message='Неопознанное сообщение!')

class ProposeNewsState(State):
    def on_enter(self, trigger):
        trigger.get_user_struct().erase_queue()
        news = newsDAO.get_news_proposed_today(trigger.current_uid)
        trigger.send_message(trigger.current_uid, message='Сегодня ты отправил {} новостей'.format(len(news)))

        if len(news) > MAX_DAILY_NEWS:
            trigger.send_message(trigger.current_uid,
                                 message='На сегодня превышен лимит отправки новостей')
            return RootState()

        # for news_i in news:
        #     trigger.send_message(trigger.current_uid, message=news_i.media)


        trigger.send_message(trigger.current_uid,
                             message='Отлично! Пиши сюда все, что нужно. Как закончишь, отправь мне стикер "Огонь"')



        trigger.send_message(trigger.current_uid, sticker_id=3007)

    def on_trigger(self, trigger):
        update = trigger.get_update()

        sticker_result = is_sticker(update)
        if sticker_result[0]:
            if sticker_result[1]=='3007':
                update = trigger.get_update()
                media_news = [entity[5] if len(entity)>5 else ''  for entity in trigger.get_user_struct().message_queue[:-1]]
                media_news = ' '.join(media_news)
                news = newsDAO.new_news(None, media_news, trigger.current_uid)
                trigger.send_message(trigger.current_uid,
                                     message='Ок, новость сохранена. Ее просмотрят администраторы, и ты получишь '
                                             'уведомление о статусе ее рассмотрения')

                moneyDAO.new_income_proposal(PROPOSAL_AMOUNT, news)
                trigger.send_message(trigger.current_uid, message='Тебе начислено {} рублей за предложение новости. '
                                                                  'Твой баланс составляет {} рублей. '
                                                                  'Подробнее в режиме "Статистика"'
                                                                  ' (отправь стикер "Расскажи-ка")'
                                     .format(PROPOSAL_AMOUNT, moneyDAO.re_count_balance(trigger.current_uid)))
                trigger.send_message(trigger.current_uid, sticker_id=4193)
                return RootState()


class StatisticsState(State):
    def on_enter(self, trigger):
        trigger.get_user_struct().erase_queue()
        trigger.send_message(trigger.current_uid, message='У тебя на счету {} рублей. Вот статус твоих постов:'
                             .format(moneyDAO.re_count_balance(trigger.current_uid)))
        news = newsDAO.news_by_blogger(trigger.current_uid)
        for i in range(len(news)):
            trigger.send_message(trigger.current_uid, message='-------------------------')
            trigger.send_message(trigger.current_uid, message='Пост №{}'.format(i+1))

            media_list=[ent.media for ent in news]
            #media_post = ' '.join(media_list)
            if len(media_list[i]) > 300:
                trigger.send_message(trigger.current_uid, message='{}...'.format(media_list[i][:30]))
            else:
                trigger.send_message(trigger.current_uid, message=media_list[i])

            review_rating =newsDAO.get_news_review_rating(news[i])
            trigger.send_message(trigger.current_uid, message='Оценено администратором: '+('Да' if review_rating!=0 else 'Нет'))
            if review_rating != 0:
                trigger.send_message(trigger.current_uid,
                                     message='Оценка: ' + 'Лайк' if review_rating == 1 else 'Дизлайк')

            trigger.send_message(trigger.current_uid, message='Опубликавано: '+('Да' if newsDAO.is_news_published(news[i]) else 'Нет'))
        return RootState()


class AdminChatState(State):
    def on_enter(self, trigger):
        trigger.get_user_struct().erase_queue()
        trigger.send_message(trigger.current_uid,
                             message='Включен режим диалога с администратором. В этом режиме бот не будет реагировать на твои команды.'
                                     ' Отправь стикер "Огонь", чтобы возобновить использование бота')

        trigger.send_message(trigger.current_uid, sticker_id=3007)

    def on_trigger(self, trigger):
        update = trigger.get_update()
        sticker_result = is_sticker(update)
        if sticker_result[0]:
            if sticker_result[1] == '3007':
                trigger.send_message(trigger.current_uid,
                                    message='Режим диалога с администратором выключен. Чтобы предложить новость, отправь стикер "Поехали",'
                                            ' а чтобы посмотреть статистику, отправь стикер "Расскажи-ка"')
                return RootState()

