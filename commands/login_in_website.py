import time
from selenium.webdriver.common.keys import Keys


def enter_in_site(driver, url, loginM, passM):
    driver.get(url)
    time.sleep(4)  # открытие ссылки

    '''Enter login'''
    number = driver.find_element('name', 'username')
    number.clear()
    number.send_keys(loginM)
    time.sleep(1)

    '''Enter password'''
    pass_m = driver.find_element('name', 'password')
    pass_m.clear()
    pass_m.send_keys(passM)
    time.sleep(1)

    '''Enter key'''
    pass_m.send_keys(Keys.ENTER)
    time.sleep(4)