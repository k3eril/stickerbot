import telebot
from telebot import types
bot = telebot.TeleBot("5551454065:AAHyY-m-mZEXIB08k5bgfgbuyMfNSyGn8zc", parse_mode=None)
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('хочу стикер')
    markup.add(itembtn1)
    itembtn2 = types.KeyboardButton('хочу другой')
    markup.add(itembtn2)
    bot.send_message(m.chat.id, "привет!!! хочешь, я пришлю тебе смешной стикер?", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "хочу стикер":
    bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEFfW5i7szHw271GsXrcfndpeXC2c01YgACbRQAAvh48Ev_35tLbqKxRykE")
  elif message.text == 'хочу другой':
    bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEFfa5i7tzDISFqRhqxUA9lHLdOcHrX2gACcw4AAsTR6EqJMDBDCLDBcSkE")
  elif message.text == "/help":
    bot.send_message(message.from_user.id, "если хочешь стикер, напиши /start или нажми на кнопку")
  else:
    bot.send_message(message.from_user.id,'напиши /help')
bot.infinity_polling()
