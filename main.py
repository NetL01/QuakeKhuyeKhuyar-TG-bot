import telebot

try:




	@bot.message_handler(commands=['start'])
	def start(message):
		bot.send_message(message.chat.id, text=f'Hello,	{message.from_user.username}!')

	@bot.message_handler(commands=['пидор_дня'.upper().lower()])
	def who_pidor(message):
		bot.send_message(message.chat.id, text=f'семен пидор дня')


	bot.polling(none_stop=True, interval=0)
except:
	print('pizdec')
