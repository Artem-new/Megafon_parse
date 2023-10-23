import pickle
import time

def get_cokies(driver):

    cookies = pickle.load(open(r"cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
        time.sleep(2)
