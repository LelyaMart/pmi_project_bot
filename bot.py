import telebot
from dclass import clas
import requests
from io import BytesIO
from PIL import Image

token = 'TOKEN'
bot = telebot.TeleBot(token)
APP_NAME = 'Pmi_project'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Отправь мне фотографию, и я скажу на какого преподавателя МИФИ ты похож.')

@bot.message_handler(content_types=['text', 'entities', 'audio', 'document', 'sticker', 'video', 'voice', 'caption', 'contact', 'location', 'venue'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Прости, я тебя не понимаю( Отправь мне фотографию")

@bot.message_handler(content_types=['photo'])
def getPhoto(message):
    bot.send_message(message.from_user.id, "Секунду...")
    fileID = message.photo[-1].file_id
    file = bot.get_file(fileID)
    path = file.file_path
    path = 'https://api.telegram.org/file/bot' + token + '/' + path
    try:
        x = clas(path)
        imag = requests.get(x[1]).content
        imag = Image.open(BytesIO(imag))
        bot.send_photo(message.from_user.id, imag, caption = x[2])
    except:
        bot.send_message(message.from_user.id, "Ой, я не нашёл твоё лицо( Отправь другую фотографию")

bot.polling(none_stop=True, interval=0)
