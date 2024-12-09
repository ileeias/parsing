import requests
from bs4 import BeautifulSoup
import telebot

bot = telebot.TeleBot('7375162409:AAHYUQGq45SR8VdeokV--IiX272UrzBO8t4')

@bot.message_handler(commands=['olx'])
def olx_search(message: telebot.types.Message):
    text1 = 'Что искать на olx?'
    bot.register_next_step_handler(message, olx_pars)
    bot.send_message(message.chat.id, text1)

def olx_pars(message):
    url = 'https://www.olx.kz/list/q-' + message.text.replace(' ', '-') + '/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('div', class_='css-1sw7q4x')[:10]
    text = ''
    for i in range(0, len(cards)):
        try:
            card_url = 'https://www.olx.kz' + cards[i].find('a', class_='css-z3gu2d')['href']
            card_adres = cards[i].find('p', class_="css-1mwdrlh").text
            card_title = cards[i].find('h6', class_='css-1wxaaza').text
            card_price = cards[i].find('p', class_='css-13afqrm').text
            text = (text + f'<i>{card_title}</i>\n' + ' - ' + f'<b>{card_price}</b>\n' + f'<u>{card_adres}</u>\n' +
                    f'<a href="{card_url}">Ссылка на товар</a>' + '\n\n')
        except AttributeError:
            break
    bot.send_message(message.chat.id, text, parse_mode='HTML')

@bot.message_handler(content_types=['text'])
def hello(message):
    bot.send_message(message.chat.id, 'Введите команду /olx')


bot.polling(non_stop=True, interval=0)