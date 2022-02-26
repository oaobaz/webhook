import os
import telebot
from telebot import types
from flask import Flask, request

TOKEN = '5036409685:AAGk9sy7hxamk0y8woYl4GQYHM4ulk5WZpI'
APP_URL = f'https://vitaljaheroku.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot('5036409685:AAGk9sy7hxamk0y8woYl4GQYHM4ulk5WZpI')
server = Flask(__name__)


def a(message):
    if message.text == 'Да':
        bot.send_message(message.from_user.id,
                         'Для уточнения информации свяжитесь с нашим менеджером по телефону +74722777001 в будни с 8.00 до 16.45 ч. или напишите на почту sale@belabraziv.ru отдела продаж.', )
        bot.send_message(message.from_user.id, "Всегда рады помочь! Спасибо за Ваше обращение!", reply_markup=keyboard1)


    else:
        bot.send_message(message.from_user.id, "Всегда рады помочь! Спасибо за Ваше обращение!", reply_markup=keyboard1)


keyboard1 = telebot.types.ReplyKeyboardMarkup(False, False)
keyboard1.row('Как разместить заказ', 'Стоимость продукции', 'Каталог товаров')
keyboard1.row('Консультация по продукции', 'Сроки изготовления продукции', 'Условия оплаты')
keyboard1.row('Способы доставки', 'Ближайший региональный дилер', 'Контакты')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Да', 'Нет')

keyboard3 = telebot.types.InlineKeyboardMarkup()
url_btn = types.InlineKeyboardButton(text='здесь', url='https://belabraziv.ru/sotrudnichestvo/')
keyboard3.add(url_btn)

keyboard4 = telebot.types.InlineKeyboardMarkup()
url_btn = types.InlineKeyboardButton(text='Скачать каталог',
                                     url='https://belabraziv.ru/useful/%D0%9A%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%20%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%86%D0%B8%D0%B8%20%D0%91%D0%90%D0%97.pdf')
keyboard4.add(url_btn)

keyboard5 = telebot.types.InlineKeyboardMarkup()
url_btn = types.InlineKeyboardButton(text='номер', url='+74722777001')
keyboard5.add(url_btn)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте,' + ' ' + message.from_user.first_name + '!\nЧто Вас интересует?',
                     reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def order(message):
    if message.text == 'Как разместить заказ':
        bot.send_message(message.from_user.id,
                         'Давайте я всё расскажу!\nВы уже определились с ассортиментом интересующей продукции?',
                         reply_markup=keyboard2)

        bot.register_next_step_handler(message, order_yes)

    elif message.text == 'Стоимость продукции':
        bot.send_message(message.from_user.id,
                         "Узнать стоимость продукции можно в презентации по ссылке\nhttps://belabraziv.ru/documents/presentation.pdf\n"
                         "Для получения детальной информации позвоните по телефону +74722777001 в будни с 8.00 до 16.45 ч. или напишите на почту sale@belabraziv.ru отдела продаж.\n")
        bot.send_message(message.from_user.id, 'Всегда рады помочь! Спасибо за Ваше обращение!')

    elif message.text == 'Каталог товаров':
        bot.send_message(message.from_user.id,
                         "Для скачивания каталога нажмите на кнопку ниже \U00002B07", reply_markup=keyboard4)
        bot.send_message(message.from_user.id, 'Остались вопросы?', reply_markup=keyboard2)
        bot.register_next_step_handler(message, catalog)

    elif message.text == 'Консультация по продукции':
        bot.send_message(message.from_user.id,
                         "Хорошо! Для связи с менеджером отдела продаж позвоните по телефону +74722777001 в будни с 8.00 до 16.45 ч."
                         )
        bot.send_message(message.from_user.id, "Всегда рады помочь! Спасибо за Ваше обращение!")

    elif message.text == 'Сроки изготовления продукции':
        bot.send_message(message.from_user.id,
                         'У нас для Вас отличная новость! Мы изготовим Вашу продукцию в течение 6 рабочих дней.')
        bot.send_message(message.from_user.id, 'Остались вопросы?', reply_markup=keyboard2)
        bot.register_next_step_handler(message, deadlines)

    elif message.text == 'Условия оплаты':
        bot.send_message(message.from_user.id,
                         "Сейчас расскажу! Отгрузка товаров или производство изделий под заказ принимаются на условиях 100% предоплаты.\n"
                         "Работаем с физическими и юридическими лицами.\n"
                         "Возможен наличный и безналичный расчет.")
        bot.send_message(message.from_user.id, 'Остались вопросы?', reply_markup=keyboard2)
        bot.register_next_step_handler(message, conditions)

    elif message.text == 'Способы доставки':
        bot.send_message(message.from_user.id,
                         "Всегда рад подсказать! Мы можем отгрузить продукцию удобной для Вас транспортной компанией, "
                         "собственным транспортом или ждем в гости по адресу:\nРоссия, г. Белгород, ул. Михайловское шоссе, 2а.")
        bot.send_message(message.from_user.id, 'Остались вопросы?', reply_markup=keyboard2)
        bot.register_next_step_handler(message, delivery)

    elif message.text == 'Ближайший региональный дилер':
        bot.send_message(message.from_user.id,
                         'Ок! Наши дилеры находятся', reply_markup=keyboard3)
        bot.send_message(message.from_user.id, 'Остались вопросы?', reply_markup=keyboard2)
        bot.register_next_step_handler(message, dealer)

    elif message.text == 'Контакты':
        bot.send_message(message.from_user.id,
                         "Хорошо! Для быстрой связи с нами позвоните по номеру +74722777001 или напишите на почту sale@belabraziv.ru отдела продаж.\n"
                         "Для личной встречи ждем по адресу:\nРоссия, г. Белгород, ул. Михайловское шоссе, 2а.")
        bot.send_message(message.from_user.id, 'Всегда рады помочь! Спасибо за Ваше обращение!')


    else:
        bot.send_message(message.from_user.id,
                         'Для уточнения информации свяжитесь с нашим менеджером по телефону +74722777001 в будни с 8.00 до 16.45 ч. или напишите на почту sale@belabraziv.ru отдела продаж.', )


def order_yes(message):
    if message.text == 'Да':
        bot.send_message(message.from_user.id, 'Отправьте заявку на почту\nsale@belabraziv.ru, где укажите:\n'
                                               '- Ваши реквизиты;\n'
                                               '- Тему письма "Заявка";\n'
                                               '- О продукции: наименование, количество, типоразмер, серию, зернистость;\n'
                                               '- Предпочтительный способ доставки;\n'
                                               '- Адрес доставки.\n\nОстались вопросы?', reply_markup=keyboard2)
        bot.register_next_step_handler(message, order_yes_second)

    else:
        bot.send_message(message.from_user.id,
                         'Для уточнения информации свяжитесь с нашим менеджером по телефону +74722777001 в будни с 8.00 до 16.45 ч. или напишите на почту sale@belabraziv.ru отдела продаж.', )
        bot.send_message(message.from_user.id, "Всегда рады помочь! Спасибо за Ваше обращение!", reply_markup=keyboard1)


def order_yes_second(message):
    a(message)

#
# def prise(message):
#     a(message)


def catalog(message):
    a(message)


def deadlines(message):
    a(message)


def conditions(message):
    a(message)


def delivery(message):
    a(message)


def dealer(message):
    a(message)


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
