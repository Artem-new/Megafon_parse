from information.tokenlist import TOKEN
import requests

def send_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)
