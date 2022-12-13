import telebot

bot = telebot.TeleBot('5849840132:AAEHFN1i-u6ZiglFRYL4jcwvL-1_R9DuKdM');

#@bot.message_handler(content_types=['text'])
#def get_text_messages(message):
#    if message.text == "кто пидор?":
#        bot.send_message(message.from_user.id, "семен пидор")
#    elif message.text == "кто шнурок?":
#        bot.send_message(message.from_user.id, "кирилл шнурок")
#    else:
#        bot.send_message(message.from_user.id, "ты че совсем плебей ебанный?")

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, text=f'Hello,	{message.from_user.username}!')

@bot.message_handler(commands=['пидор_дня'.upper().lower()])
def who_pidor(message):
	bot.send_message(message.chat.id, text=f'семен пидор дня')


bot.polling(none_stop=True, interval=0)

