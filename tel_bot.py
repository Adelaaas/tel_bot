import telebot
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
import pandas as pd

bot = telebot.TeleBot('1786855905:AAGhI5rJX-StfEnQfNVQsh3RVSm5Z4EaTYw')

df = pd.read_csv('test5_1.csv')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот, созданный помогать студентам НИЯУ МИФИ. Приятно познакомиться, {message.from_user.first_name}')


# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, что ты хочешь узнать?")
        bot.send_message(message.from_user.id, df.iloc[0,1])
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_dom_oplata = types.InlineKeyboardButton(text='Как оплатить общежитие онлайн?', callback_data='dominotory')
        # И добавляем кнопку на экран
        keyboard.add(key_dom_oplata)
        key_dom_kvit = types.InlineKeyboardButton(text='Как получить квитанцию на оплату общежития онлайн?', callback_data='dom_kvit')
        # И добавляем кнопку на экран
        keyboard.add(key_dom_kvit)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери интересующий вопрос', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "dominotory": 
        # Формируем гороскоп
        msg1 = '1. Зайти в интернет-банк или мобильное приложение «ИПБ-Онлайн»'
        msg2 = '2. В разделе «Платежи и переводы» перейти в подраздел «Банковские операции»'
        msg3 = '3. Выбрать нужную услугу – «МИФИ (Общежитие, коммунальные и образовательные услуги)» или «МИФИ (Прочие услуги)»'
        msg4 = '4. На форме оплаты выбрать назначение платежа, ввести внутренний счет (указан в квитанции), номер договора (при наличии) и ФИО (при оплате за третье лицо)'
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg1 + '\n' + msg2+ '\n' + msg3 + '\n' + msg4)
        bot.send_photo(call.message.chat.id, photo=open('оплата-01.png', 'rb'))
    if call.data == "dom_kvit": 
        # Формируем гороскоп
        msg1 = '1. Зайти в раздел сервисы на home.mephi.ru'
        msg2 = '2. Выбери "Квитанции на оплату общежития"'
        msg3 = '3. Выбери необходимы период, за который хочешь оплатить общагу'
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg1 + '\n' + msg2+ '\n' + msg3)
        bot.send_photo(call.message.chat.id, photo=open('квитанция онлайн.png', 'rb'))
bot.polling(none_stop=True)