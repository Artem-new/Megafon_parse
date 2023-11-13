from information.logon import passM, loginM  # Логин пароль файла
from information.agents import user_agent_list
from information.numerlist import numbers
from information.pagelist import pages, url
from commands.login_in_website import enter_in_site
from commands.send_info import send_message
from information.chats import chat_id, chat_info
from commands.parse_website import check_numbers, balance_list, balance_value
from commands.save_information_in_json import save_to_json
import random
import requests
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from datetime import date


def check():
    try:
        '''Настрока вебдрайвера, скрывать окно браузера, убрать загрузку картинок,
        '''
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(
            f"user-agent={random.choice(user_agent_list)}")
        service = Service(executable_path='./chromedriver.exe')
        driver = webdriver.Chrome(
            service=service,
            options=options

        )
        '''Выполнение аунтификации на сайте'''
        enter_in_site(driver, url, loginM, passM)
        '''Get sites where information'''
        cheking = dict(zip(pages, numbers))
        '''Parse sites'''
        [check_numbers(item[0], item[1], driver, chat_info, chat_id)for item in cheking.items()]
        print(balance_value)



        send_message(chat_id,  '.'.join(balance_list))
        driver.quit()


    except Exception as ex:
        print(ex)
        send_message(chat_id, "Бот неисправен")


def check_url():
    test = requests.get(url)

    if test:
        print('Сайт доступен')
        check()
    else:
        send_message(chat_id, "Сайт не доступен")
        print('Сайт не доступен')


if __name__ == '__main__':
    check_url()