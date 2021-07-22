import os
import time
import pickle
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MobileBgClass():

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)
        self.load_cookies()

    def login(self):

        self.browser.get(
            'https://www.mobile.bg/pcgi/mobile.cgi?act=16&logact=1')

        try:
            cookie_consent_button = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'fc-cta-consent')))
            cookie_consent_button.click()

            email = config('MOBILE_BG_EMAIL')
            password = config('MOBILE_BG_PASSWORD')

            login_type_button = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="2"]')))
            login_type_button.click()

            email_input = WebDriverWait(self.browser, 30).until(
                EC.visibility_of_element_located((By.NAME, 'usr')))
            email_input.send_keys(email)

            password_input = WebDriverWait(self.browser, 30).until(
                EC.visibility_of_element_located((By.NAME, 'pwd')))
            password_input.send_keys(password)

            button = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'loginButton')))
            button.click()

            WebDriverWait(self.browser, 30).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'exit')))

            pickle.dump(self.browser.get_cookies(),
                        open("mobile_bg_cookies.pkl", "wb"))
        except BaseException as e:
            print(f'Something went wrong while logging you in! - {e}')

    def load_cookies(self):
        try:
            self.browser.get('https://www.mobile.bg/')
            cookies = pickle.load(open('mobile_bg_cookies.pkl', 'rb'))

            for cookie in cookies:
                self.browser.add_cookie(cookie)

            self.browser.refresh()
        except Exception:
            self.login()


instance = MobileBgClass()
