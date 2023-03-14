import telebot

bot = telebot.TeleBot("6137754016:AAHgUOjXZYbsTw9B8OH5GJfoA0pr_l6i-mY")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот Курмангазиевой Румии ИДБ-19-03. Для начала работы используйте команду /motivate")


@bot.message_handler(commands=['motivate'])
def motivate(message):
    import requests
    import random
    response = requests.get("https://type.fit/api/quotes")
    data = response.json()
    quote = random.choice(data)
    bot.send_message(message.chat.id, f"Вот вдохновляющая цитата для вас: \n\n<b>\"{quote['text']}\"</b>\n\n- {quote['author']}", parse_mode="HTML")


bot.polling()
