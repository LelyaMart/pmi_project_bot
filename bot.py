import telebot
from dclass import clas

token = '2004464512:AAHKsEHWRIds5xJwjByM1mhQ1bawEEWKwhY'
bot = telebot.TeleBot(token)
APP_NAME = 'Pmi_project'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Отправь мне фотографию, и я скажу на какого преподавателя МИФИ ты похож.')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Прости, я тебя не понимаю( Отправь мне фотографию")

@bot.message_handler(content_types=['photo'])
def getPhoto(message):
    bot.send_message(message.from_user.id, "Секунду...")
    fileID = message.photo[-1].file_id
    file = bot.get_file(fileID)
    path = file.file_path
    path = 'https://api.telegram.org/file/bot' + token + '/' + path
    x = clas(path)
    bot.send_photo(message.from_user.id, x[1])

bot.polling(none_stop=True, interval=0)
