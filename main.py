import requests

from bs4 import BeautifulSoup

from lib.Obter_mensagens import Obter_mensagens
from lib.Menu import Menu

soup = BeautifulSoup()

URL = "https://www.buscape.com.br"

hearders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/96.0.4664.110 Safari/537.36'}

site = requests.get(URL, headers=hearders)

soup = BeautifulSoup(site.content, 'html.parser')

title = soup.find_all('h2', class_='Text_Text__VJDNU Text_LabelSmRegular__qvxsr')
value = soup.find_all('strong', class_='Text_Text__VJDNU Text_LabelMdBold__uMr7_ CellPrice_MainValue__JXsj_')
installment = soup.find_all('span', class_='CellPrice_Installments__XpK2h')
link = soup.find_all('a', class_='Cell_Content__fT5st')
image = soup.find_all('img', class_='Cell_Image__K_7_C')

atributos = [title, value, installment, link, image]
update_id = None

while True:
    atualizacao = Obter_mensagens(update_id)
    mensagens = atualizacao["result"]
    if mensagens:
        for mensagem in mensagens:
            try:
                update_id = mensagem["update_id"]
                chat_id = mensagem["message"]["from"]["id"]
                nome = mensagem["message"]["from"]["first_name"]
                texto = mensagem["message"]["text"]
            except:
                chat_id = 0
                nome = ''
                texto = ''

        print(nome + " [" + str(chat_id) + "]: " + texto)

        if chat_id != 1493144474:
            try:
                with open('logs.txt', 'a') as arquivo:
                    arquivo.write(nome + " [" + str(chat_id) + "]: " + texto + "\n")
            except:
                pass
        else:
            pass

        Menu(URL, texto, chat_id, atributos)
