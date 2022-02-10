import requests
import log


def send(bot_message):
    bot_token = 'AAFn-BTZo-RB7W-oZpwNKUGw-E8W5kX6168'
    bot_chatid = '740348827'
    send_text = 'https://api.telegram.org/bot'+bot_chatid+':'+bot_token+'/sendMessage'
    text = 'Statistica - {}'.format(bot_message)
    pload = {'chat_id': '124638986', 'text': text, 'parse_mode': 'Markdown'}
    response = requests.post(send_text, data=pload)
    if response.status_code == 200:
        return response.json()
    else:
        errortext = 'Ошибка отправки в Telegram: {}'.format(response.json())
        log.warning(errortext)
