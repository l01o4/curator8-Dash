import telebot

bot = telebot.TeleBot('6481107110:AAGtYGi0nJytNaWX9b-DxRER-Ob1scMOoPE')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, напиши /help для ознакомления со всеми командами')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '/start - запуск бота, /help - список всех команд, /theory - определения')

@bot.message_handler(commands=['theory'])
def main(message):
    bot.send_message(message.chat.id,
                     'python - язык программирования, который широко используется в интернет-приложениях, разработке ПО, науке и данных и машиннос обучении')

bot.infinity_polling()