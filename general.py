import pickle
import time
import random

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent


class MiningBot:
    def __init__(self, name: str):

        """Инициализация браузера и подготовка необходимых параметров"""

        useragent = UserAgent()
        options = webdriver.FirefoxOptions()
        options.add_argument(f"User-Agent={useragent.random}")
        self.cookie = pickle.load(open(f'{name}', 'rb'))
        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 1260)
        print(name)
        self.__loging()

    def __loging(self):

        """Авторизация в кошельке с применением кукков"""

        self.driver.get("#")
        for c in self.cookie:
            self.driver.add_cookie(c)
        time.sleep(random.randint(5, 8))
        self.driver.refresh()

    def mining(self):

        """Запуск майнинга"""

        self.driver.get("#")
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-15hjstb"))).click()
        print('Successful authorization')

        while True:
            time.sleep(random.randint(10, 30))
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-2bpqia'))).click()
            print(f'Click Mine')
            time.sleep(random.randint(2, 7))
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-1szn3p1'))).click()
            print(f'Click Submit')


if __name__ == '__main__':
    start = MiningBot(input("Account name: "))
    start.mining()
    start.driver.close()
    start.driver.quit()
