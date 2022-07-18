import urllib.request
import random

from lib.Responder import Responder
from lib.Encurtar_URL import Encurtar_URL


def Menu(URL, texto, chat_id, atributos):
    title = atributos[0]
    value = atributos[1]
    installment = atributos[2]
    link = atributos[3]
    image = atributos[4]

    menu = "🛍 BEM VINDO AO SÓ PROMÔ!\n\n\nEscolha uma opção:\n\n1⃣ - Promoções\n\n2⃣ - Avalie o SÓ PROMÔ\n\n3️⃣ - Sobre"

    Responder('text', menu, chat_id, None)

    if str(texto) == '1':
        for i in range(0, 8):
            promo_random = random.randint(0, len(title) - 1)
            try:
                url_short = Encurtar_URL(URL, link[promo_random])
            except:
                url_short = URL + link[promo_random].get('href')

            try:
                promocao = (title[promo_random].text + '\n\n🔥 ' + value[promo_random].text + '\n' + '💳 ' +
                            installment[promo_random].text + '\n🛍️ ' + url_short + '\n')
            except:
                pass

            Responder('text', promocao, chat_id, None)

        Responder('text', '➕ Digite 1⃣  para ver mais promoções.\n\n'
                          '⭐ Digite 2️⃣ para avaliar o SÓ PROMÔ.', chat_id, None)
    elif str(texto) == '2':
        rate_text = "⭐ Avalie a sua esperiência com o SÓ PROMÔ\n\n👉 https://forms.gle/Kku8U538tfAWyDra8"
        Responder('text', rate_text, chat_id, None)
    elif str(texto) == '3':
        about_text = "🤑 Este é um robô desenvolvido para trazer as melhores ofertas aos viciados em promoções.\n\n" \
                     "Digite 1⃣  e venha conferir as melhores promoções que separamos para você! 🔥"

        Responder('text', about_text, chat_id, None)

    elif str(texto) == '/start':
        pass
    else:
        Responder('text', '⚠️Opção desconhecida, tente novamente!', chat_id, None)
