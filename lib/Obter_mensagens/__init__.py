import requests
import json

token = '5065125335:AAGz1c_DxdFMtQvM6GymfhuL5VSBYtQZd3Q'
url_base = f'https://api.telegram.org/bot{token}/'

def Obter_mensagens(update_id):
    link_requisicao = f'{url_base}getUpdates?timeout=100'
    if update_id:
        link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)