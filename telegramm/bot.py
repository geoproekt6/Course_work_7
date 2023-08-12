import os
import requests


class TeleBotApi:
    TOKEN = os.getenv('BOT_TOKEN')
    URL = f'https://api.telegram.org/bot{TOKEN}'

    @classmethod
    def __get_chat_id(cls):
        """Получить чат id"""
        url_for = cls.URL + '/getUpdates'
        responce = requests.get(url_for).json()
        print(responce)
        return responce.get('result')[0].get('message').get('chat').get('id')

    @classmethod
    def send_message(cls, **datas):
        text = f'Я буду {datas["action"]} в {datas["times"]} в {datas["place"]}'
        data = {
            'chat_id': cls.__get_chat_id(),
            'text': text,
        }
        responce = requests.get(cls.URL + '/sendMessage', data)
        print(responce.json)
