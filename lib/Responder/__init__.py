import requests

token = '5065125335:AAGz1c_DxdFMtQvM6GymfhuL5VSBYtQZd3Q'
url_base = f'https://api.telegram.org/bot{token}/'

def Responder(tipo, resposta, chat_id, files):
    if tipo == 'text':
        link_de_envio = f'{url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio)
    elif tipo == 'image':
        resp = requests.post(url_base + 'sendPhoto?chat_id=' + str(chat_id) + '&caption=' + resposta, files=files)
        print(resp.status_code)
    else:
        pass