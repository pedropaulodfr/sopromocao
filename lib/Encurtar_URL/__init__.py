import requests
import json

def Encurtar_URL(URL, link):
    api_base = f"https://api.shrtco.de/v2/shorten?url={URL + link.get('href')}/very/long/link.html"
    answer = requests.get(api_base).json()
    return answer["result"]["short_link"]