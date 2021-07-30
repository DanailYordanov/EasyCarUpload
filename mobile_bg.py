import os
import pickle
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class images_uploaded():
    """An expectation for checking that all images are uploaded"""

    def __init__(self, images_number):
        self.images_number = images_number

    def __call__(self, driver):
        images = driver.find_elements_by_xpath(
            '//div[@style and @class="photo"]')
        if len(images) == self.images_number:
            return images
        else:
            return False


class options_present():
    """An expectation for checking that all select options are present"""

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        select = driver.find_element(*self.locator)
        select = Select(select)
        if len(select.options) > 1:
            return select
        else:
            return False


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
                EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="1"]')))
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

    def choose_brand(self, choice):
        try:
            brand_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'f5')))
            brand_select = Select(brand_select)
            brand_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a brand ! - {e}')

    def choose_model(self, choice):
        try:
            model_select = WebDriverWait(self.browser, 30).until(
                options_present((By.NAME, 'f6')))
            model_select = Select(model_select)
            model_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a model ! - {e}')

    def input_modification(self, input):
        if input:
            try:
                modification_input = self.browser.find_element_by_name(
                    'f7')
                modification_input.send_keys(input)
            except BaseException as e:
                print(
                    f'Something went wrong while inputting a modification ! - {e}')

    def choose_category(self, choice):
        try:
            category_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'f11')))
            category_select = Select(category_select)
            category_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a category ! - {e}')

    def input_price(self, input):
        try:
            price_input = self.browser.find_element_by_name('f12')
            price_input.send_keys(input)
        except BaseException as e:
            print(f'Something went wrong while inputting a price ! - {e}')

    def choose_transmission_type(self, choice):
        if choice == 'Автоматични':
            choice = 'Автоматична'
        elif choice == 'Ръчни':
            choice = 'Ръчна'

        try:
            transmission_type_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'f10')))
            transmission_type_select = Select(transmission_type_select)
            transmission_type_select.select_by_visible_text(choice)
        except BaseException as e:
            print(
                f'Something went wrong while choosing a transmission type! - {e}')

    def choose_fuel_type(self, choice):
        if choice == 'Бензин':
            choice = 'Бензинов'
        elif choice == 'Дизел':
            choice = 'Дизелов'
        elif choice == 'Хибрид':
            choice = 'Хибриден'
        elif choice == 'Електричество':
            choice = 'Електрически'

        try:
            fuel_type_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'f8')))
            fuel_type_select = Select(fuel_type_select)
            fuel_type_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a fuel type ! - {e}')

    def input_power(self, input):
        if input:
            try:
                power_input = self.browser.find_element_by_name('f9')
                power_input.send_keys(input)
            except BaseException as e:
                print(f'Something went wrong while inputting power ! - {e}')

    def choose_month(self, choice):
        choice = choice.lower()

        try:
            month_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'f14')))
            month_select = Select(month_select)
            month_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a month ! - {e}')

    def choose_year(self, choice):
        try:
            year_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'f15')))
            year_select = Select(year_select)
            year_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a year ! - {e}')

    def input_run(self, input):
        try:
            run_input = self.browser.find_element_by_name('f16')
            run_input.send_keys(input)
        except BaseException as e:
            print(f'Something went wrong while inputting run ! - {e}')

    def choose_color(self, choice):
        if choice:
            try:
                color_select = WebDriverWait(self.browser, 30).until(
                    EC.element_to_be_clickable((By.NAME, 'f17')))
                color_select = Select(color_select)
                color_select.select_by_visible_text(choice)
            except BaseException as e:
                print(f'Something went wrong while choosing a color ! - {e}')

    def choose_euro_standart(self, choice):
        if choice:
            choice = 'Евро ' + choice[-1]

            try:
                euro_standart_select = WebDriverWait(self.browser, 30).until(
                    EC.element_to_be_clickable((By.NAME, 'f29')))
                euro_standart_select = Select(euro_standart_select)
                euro_standart_select.select_by_visible_text(choice)
            except BaseException as e:
                print(
                    f'Something went wrong while choosing a EURO standart ! - {e}')

    def input_description(self, input):
        if input:
            try:
                description_input = self.browser.find_element_by_name('f21')
                description_input.send_keys(input)
            except BaseException as e:
                print(
                    f'Something went wrong while inputting a description ! - {e}')

    def choose_region(self, choice):
        try:
            region_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'f18')))
            region_select = Select(region_select)
            region_select.select_by_visible_text(choice)
        except BaseException as e:
            print(
                f'Something went wrong while choosing a region ! - {e}')

    def choose_city(self, choice):
        try:
            city_select = WebDriverWait(self.browser, 30).until(
                options_present((By.NAME, 'f19')))
            city_select.select_by_visible_text(choice)
        except BaseException as e:
            print(
                f'Something went wrong while choosing a city ! - {e}')

    def input_phone_number(self, input):
        try:
            phone_number_input = self.browser.find_element_by_name('f22')
            phone_number_input.send_keys(input)
        except BaseException as e:
            print(
                f'Something went wrong while inputting a phone number ! - {e}')

    def upload_images(self, paths):
        try:
            # When you join all paths with \n you can pass them to the input at once

            multiple_images_path = '\n'.join(paths)
            image_input = self.browser.find_element_by_xpath(
                '//input[@type="file"]')
            image_input.send_keys(multiple_images_path)

            # Wait for the images to upload

            WebDriverWait(self.browser, 30).until(
                images_uploaded(len(paths)))
        except BaseException as e:
            print(f'Something went wrong while uploading images ! - {e}')

    def publish(self, category, brand, model, modification, price,
                transmission_type, fuel_type, power, year, month, run,
                color, euro_standart, description, image_paths, phone_number):

        self.browser.get(
            'https://www.mobile.bg/pcgi/mobile.cgi?pubtype=1&act=6&subact=4&actions=1')

        self.choose_brand(brand)

        self.choose_model(model)

        self.input_modification(modification)

        self.choose_fuel_type(fuel_type)

        self.input_power(power)

        self.choose_euro_standart(euro_standart)

        self.choose_transmission_type(transmission_type)

        self.choose_category(category)

        self.input_price(price)

        self.choose_month(month)

        self.choose_year(year)

        self.input_run(run)

        self.choose_color(color)

        self.choose_region('Дупница')

        self.choose_city('с. Блатино')

        self.input_description(description)

        self.input_phone_number(phone_number)

        price_change_checkbox = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.NAME, 'f28')))
        price_change_checkbox.click()

        publish_advert_checkbox = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mainholder"]/table[6]/tbody/tr/td/form/table[4]/tbody/tr[3]/td/input[2]')))
        publish_advert_checkbox.click()

        button = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="button"]')))
        button.click()

        add_photos_button = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/table[6]/tbody/tr/td/table[2]/tbody/tr/td[3]/table[1]/tbody/tr/td[2]/input')))
        add_photos_button.click()

        self.upload_images(image_paths)

        offer_button = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/table[3]/tbody/tr/td[1]/a[3]')))
        offer_button.click()

        offer_link = self.browser.find_element_by_class_name('advpage')
        offer_link = offer_link.get_attribute('value')

        self.browser.get(offer_link)
