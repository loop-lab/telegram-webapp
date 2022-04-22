import telebot

bot = telebot.TeleBot('5380014713:AAFUi3QkzPPPINxO20vUHXbrzIWC0AJEkvM');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, message.text)


bot.polling(none_stop=True, interval=0)