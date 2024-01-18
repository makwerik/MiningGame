import pickle
import time
import random
import datetime


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
        options.add_argument('--headless')
        self.cookie = pickle.load(open(f'{name}', 'rb'))
        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 1260)
        self.wait_confirm = WebDriverWait(self.driver, 5)
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
        window_main = self.driver.window_handles[0]
        print('Successful authorization')

        try:
            time.sleep(10)
            window_confirmation_logging = self.driver.window_handles[-1]
            self.driver.switch_to.window(window_confirmation_logging)
            self.wait_confirm.until(EC.presence_of_element_located((
                By.CSS_SELECTOR,
                'html body.fontLoaded div#root div.sc-1pggoe8-0.ihvWJS div.authorize-read-name-container '
                'label.ant-checkbox-wrapper.action-check span.ant-checkbox input.ant-checkbox-input'))).click()
            time.sleep(3)
            self.wait_confirm.until(EC.presence_of_element_located((
                By.CSS_SELECTOR,
                '.sc-vuxumm-0 > button:nth-child(1)'))).click()
            self.driver.switch_to.window(window_main)
        except:
            self.driver.switch_to.window(window_main)
            print('Automaric confirmation is not required')

        try:
            name = self.wait_confirm.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div[1]/div[2]/div[2]/p"))).text
            print(name)
        except:
            print('You are not logged in to your account')
            return None

        while True:
            time.sleep(random.randint(10, 30))
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-2bpqia'))).click()
            print(f'Click Mine')
            time.sleep(random.randint(2, 7))
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-1szn3p1'))).click()
            print(f'Click Submit')

            try:
                time.sleep(10)
                window_after = self.driver.window_handles[-1]
                self.driver.switch_to.window(window_after)
                self.wait_confirm.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ant-checkbox-input'))).click()
                time.sleep(3)
                self.wait_confirm.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-vuxumm-0 > button:nth-child(1)'))).click()
                self.driver.switch_to.window(window_main)
            except:
                self.driver.switch_to.window(window_main)
                print('Confirmation is not required')


if __name__ == '__main__':
    start = MiningBot(input("Account name: "))
    start.mining()
    start.driver.close()
    start.driver.quit()
