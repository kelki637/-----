import requests
from bs4 import BeautifulSoup as BS
import random
import telebot
from telebot import types

TOKEN = '6019917703:AAGXtjQrP3QWvRgj0jmamaMmUZhZOs1MBA4'
URL = "https://www.anekdot.ru/random/anekdot/"
URLprill = 'https://www.anekdot.ru/last/good/'
#фyнкции
def parser(url):
    r = requests.get(url)
    soup = BS(r.text, "html.parser")
    anekdots = soup.find_all('div', class_= "text")
    return [i.text for i in anekdots]

list_anekdots = parser(URL)
random.shuffle(list_anekdots)

def parser_prill(url):
    r = requests.get(url)
    soup = BS(r.text, "html.parser")
    anekdots = soup.find_all('div', class_= "text")
    return [i.text for i in anekdots]

list_prill = parser_prill(URLprill)
random.shuffle(list_prill)

#бот
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def hello(message):
    markup_inline = types.InlineKeyboardMarkup()
    intem_rand = types.InlineKeyboardButton(text='Рандомная шутка', callback_data="rand")
    item_pril = types.InlineKeyboardButton(text='Рандомная шутка(приличная)', callback_data="randpril")

    markup_inline.add(intem_rand, item_pril)
    bot.send_message(message.chat.id,'Привет',reply_markup = markup_inline)

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == "rand":
        bot.send_message(call.message.chat.id, list_anekdots[0])
        del list_anekdots[0]
    elif call.data == "randpril":
        bot.send_message(call.message.chat.id, list_prill[0])
        del list_prill[0]
        

bot.polling(none_stop = True, interval = 0)



