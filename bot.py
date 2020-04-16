import telebot
import requests, json

token = "1148004707:AAHv-pALIVTq7yQKeSGpDHCvoY7Kb6HK6Is" 
bot = telebot.TeleBot(token)

# TODO add menus to bot

@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        url = "http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=3eb5774c79e43a964b30a62cbe2df703" % (message.location.latitude, message.location.longitude)
        request = requests.get(url)
        data = dict(request.json())
        temp = str(int(data["main"]["temp"]) - 272)
        name = data["name"]
        bot.send_message(message.chat.id, "Current temperature in " + name  + " is " + temp)

bot.polling()