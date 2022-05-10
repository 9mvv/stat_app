import requests
import log
from os import environ

bot_token = environ['BOT_TOKEN']
bot_chatid = environ['BOT_CHAT_ID']

def send(bot_message):
    send_text = 'https://api.telegram.org/bot'+bot_chatid+':'+bot_token+'/sendMessage'
    text = 'Statistica - {}'.format(bot_message)
    pload = {'chat_id': '124638986', 'text': text, 'parse_mode': 'Markdown'}
    response = requests.post(send_text, data=pload)
    if response.status_code == 200:
        return response.json()
    else:
        errortext = 'Ошибка отправки в Telegram: {}'.format(response.json())
        log.warning(errortext)
