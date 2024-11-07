import telebot
import requests
import json


bot = telebot.TeleBot("8122469189:AAHDZaq7q-ofDe9GfusiFc2TU43qGRI01_E")
API = "3688810fa13b27b6da3d92d29f77ca1f"


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}")
    bot.send_message(message.chat.id, "Напиши город, я расскажу о его погоде")


@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f"Сейчас погода: {temp}")

        if temp > 5.0 and temp < 20.0:
            file = open('./погода_3.jpeg', 'rb')
            bot.send_photo(message.chat.id, file)
        elif temp > 20.0:
            file_2 = open('./погода_02.jpeg', 'rb')
            bot.send_photo(message.chat.id, file_2)
        else:
            file_3 = open('./погода_2.jpeg', 'rb')
            bot.send_photo(message.chat.id, file_3)


    else:
        bot.reply_to(message, "Город указан не верно !!!")




bot.polling(none_stop=True)