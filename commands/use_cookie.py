import pickle
def useing_cookies(driver):
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    # driver.quit()
    cookies = pickle.load(open("cookies.pkl", "rb"))