import telebot
import requests
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Котика!'))
keyboard.add(KeyboardButton('Гифку котика!'))


@bot.message_handler(content_types=['photo', 'video', 'sticker', 'gif'])
def say_error(message):
    bot.send_message(message.chat.id, 'Я не поддерживаю данный тип данных 😢')


@bot.message_handler(regexp=r'[Гг]иф')
def send_cat(message):
    content = requests.get('https://cataas.com/cat/gif?json=true').json()
    bot.send_document(message.chat.id, 'cataas.com' + content['url'], reply_markup=keyboard)


@bot.message_handler(regexp=r'[Кк]от')
def send_cat(message):
    content = requests.get('https://cataas.com/cat').content
    bot.send_photo(message.chat.id, content, reply_markup=keyboard)


@bot.message_handler()
def say_hello(message):
    bot.send_message(message.chat.id, 'Я - бот, отправляющий котиков!', reply_markup=keyboard)


bot.infinity_polling()
