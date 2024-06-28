# from telebot import TeleBot, types

# bot = TeleBot('6704792126:AAGpqxtc36goOtl62kKQpCSXEzp9d2sQ-iY')

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Tolov otkazmoqchi bolgan sumangizni kiriting.")

# @bot.message_handler(func=lambda message : True)
# def open_modal(message):
#     print(message.text)
#     markup = types.InlineKeyboardMarkup()
#     web_app_info = types.WebAppInfo(url=f"https://my.click.uz/services/pay/?service_id=9930&merchant_id=7366&amount={message.text}.00&transaction_param=379208&return_url=https%3A%2F%2Fclients.ahost.uz%2Fviewinvoice.php%3Fid%3D379208&merchant_user_id=8895")
#     web_app_button = types.InlineKeyboardButton(text="Tolovni otkazish", web_app=web_app_info)
#     markup.add(web_app_button)
#     bot.send_message(message.chat.id, "Click the button to open a modal window:", reply_markup=markup)

# bot.polling()


from telebot import TeleBot, types

bot = TeleBot('6704792126:AAGpqxtc36goOtl62kKQpCSXEzp9d2sQ-iY')



# @bot.inline_handler(lambda query: len(query.query) > 0)
# def query_text(query):
#     try:
#         result = types.InlineQueryResultArticle(
#             id='1',
#             title="Search Result",
#             input_message_content=types.InputTextMessageContent(message_text="You searched for: " + query.query)
#         )
#         bot.answer_inline_query(query.id, [result], cache_time=1)
#     except Exception as e:
#         print(f"Error: {e}")

# bot.polling()


# translations = {
#     "hello": ["привет", "здравствуйте","ifjfggg"],
#     "world": ["мир", "вселенная"],
#     "example": ["пример", "образец"],
# }

# # Обработчик inline-запросов
# @bot.inline_handler(lambda query: len(query.query) > 0)
# def query_text(query):
#     try:
#         query_text = query.query.lower()
#         results = []

#         if query_text in translations:
#             for i, translation in enumerate(translations[query_text]):
#                 result = types.InlineQueryResultArticle(
#                     id=str(i),
#                     title=f"Translation for '{query_text}': {translation}",
#                     input_message_content=types.InputTextMessageContent(
#                         message_text=f"The translation of '{query_text}' is: {translation}"
#                     ),
#                     description=f"Translation: {translation}"
#                 )
#                 results.append(result)
#         else:
#             result = types.InlineQueryResultArticle(
#                 id='0',
#                 title="No translation found",
#                 input_message_content=types.InputTextMessageContent(
#                     message_text=f"No translation found for '{query_text}'"
#                 ),
#                 description="Try a different word."
#             )
#             results.append(result)

#         bot.answer_inline_query(query.id, results, cache_time=1)
#     except Exception as e:
#         print(f"Error: {e}")

# bot.polling()

@bot.message_handler(commands=['poll'])
def send_poll(message):
    question = "What's your favorite programming language?"
    options = ["Python", "JavaScript", "Java", "C++"]
    bot.send_poll(message.chat.id, question, options)

bot.polling()