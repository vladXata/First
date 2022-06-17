import telebot

bot = telebot.TeleBot("5407756574:AAGPUcYivO4ez4EP6lkSzE_APMKp-wzHcqI", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(content_types=['text'])
def send_echo(message):
	# bot.reply_to(message, message.text)
        bot.send_message(message.chat.id, message.text)
bot.polling( none_stop = True)
