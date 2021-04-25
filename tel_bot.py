import telebot
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

bot = telebot.TeleBot('1786855905:AAGhI5rJX-StfEnQfNVQsh3RVSm5Z4EaTYw')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот, созданный помогать студентам НИЯУ МИФИ. Приятно познакомиться, {message.from_user.first_name}')


# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, что ты хочешь узнать?.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Как оплатить общежитие онлайн?', callback_data='dominotory')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
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
        msg = 'Зайти в раздел "Сервисы" на home.mephi.ru'
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, photo=open('bee-on-daisy.jpg', 'rb'))

bot.polling(none_stop=True)