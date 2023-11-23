import time
from selenium.webdriver.common.keys import Keys

"""Поиск элементов на странице и ввод логина и пароля"""
def enter_in_site(driver, url, loginM, passM):
    driver.get(url)
    time.sleep(20)  # открытие ссылки

    '''Enter login'''
    number = driver.find_element('name', 'username')
    number.clear()
    number.send_keys(loginM)

    '''Enter password'''
    pass_m = driver.find_element('name', 'password')
    pass_m.clear()
    pass_m.send_keys(passM)

    '''Enter key'''
    pass_m.send_keys(Keys.ENTER)
    time.sleep(4)