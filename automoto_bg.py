from selenium.webdriver.support.ui import Select
from selenium import webdriver
from decouple import config
import time
import pickle


class AutomotoBg():

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.load_cookies()

    def login(self):

        self.browser.get('https://automoto.bg/login')

        time.sleep(5)

        cookie_consent_button = self.browser.find_element_by_class_name(
            'cc-btn')
        cookie_consent_button.click()

        time.sleep(1)

        email = config('AUTOMOTO_BG_EMAIL')
        password = config('AUTOMOTO_BG_PASSWORD')

        email_input = self.browser.find_element_by_name('email')
        email_input.send_keys(email)

        time.sleep(0.5)

        password_input = self.browser.find_element_by_name('password')
        password_input.send_keys(password)

        time.sleep(0.5)

        button = self.browser.find_element_by_xpath(
            '//*[@id="content"]/div/div/div[2]/section/form/div[2]/label/button')
        button.click()

        time.sleep(1)

        pickle.dump(self.browser.get_cookies(),
                    open('automoto_bg_cookies.pkl', 'wb'))

    def load_cookies(self):
        try:
            self.browser.get('https://automoto.bg/')
            cookies = pickle.load(open('automoto_bg_cookies.pkl', 'rb'))

            for cookie in cookies:
                self.browser.add_cookie(cookie)

            time.sleep(1)

            self.browser.refresh()

            time.sleep(5)

        except Exception:
            self.login()

    def add(self, category, brand, model, engine_type, price,
            gear_type, fuel_type, power, cubature, year, month, run,
            doors_type, color, euro_type, description, image_paths):

        self.browser.get('https://automoto.bg/listings/create')

        time.sleep(5)

        brand_select = Select(self.browser.find_element_by_name('mark_id'))
        brand_select.select_by_visible_text(brand)

        time.sleep(1)

        model_select = Select(self.browser.find_element_by_name('model_id'))
        model_select.select_by_visible_text(model)

        time.sleep(1)

        engine_type_input = self.browser.find_element_by_name('modification')
        engine_type_input.send_keys(engine_type)

        time.sleep(1)

        category_select = Select(self.browser.find_element_by_name('coupe_id'))
        category_select.select_by_visible_text(category)

        price_input = self.browser.find_element_by_name('price')
        price_input.send_keys(price)

        time.sleep(1)

        gear_type_select = Select(
            self.browser.find_element_by_name('speed_id'))
        gear_type_select.select_by_visible_text(gear_type)

        time.sleep(1)

        fuel_type_select = Select(self.browser.find_element_by_name('fuel_id'))
        fuel_type_select.select_by_visible_text(fuel_type)

        time.sleep(1)

        power_input = self.browser.find_element_by_name('power')
        power_input.send_keys(power)

        time.sleep(1)

        cubature_input = self.browser.find_element_by_name('cubic')
        cubature_input.send_keys(cubature)

        time.sleep(1)

        month_select = Select(self.browser.find_element_by_name('month_id'))
        month_select.select_by_visible_text(month)

        time.sleep(1)

        year_select = Select(self.browser.find_element_by_name('year_id'))
        year_select.select_by_visible_text(year)

        time.sleep(1)

        run_input = self.browser.find_element_by_name('mileage')
        run_input.send_keys(run)

        time.sleep(1)

        doors_type_select = Select(
            self.browser.find_element_by_name('door_id'))
        doors_type_select.select_by_visible_text(doors_type)

        time.sleep(1)

        color_select = Select(self.browser.find_element_by_name('color_id'))
        color_select.select_by_visible_text(color)

        time.sleep(1)

        euro_type_select = Select(
            self.browser.find_element_by_name('euro_standart_id'))
        euro_type_select.select_by_visible_text(euro_type)

        time.sleep(1)

        description_input = self.browser.find_element_by_name('description')
        description_input.send_keys(description)

        time.sleep(1)

        for path in image_paths:
            image_input = self.browser.find_element_by_xpath(
                '//input[@type="file"]')
            image_input.send_keys(path)
            time.sleep(2)


paths = []

instance = AutomotoBg()
instance.add('Седан', 'BMW', '335', '335i', '20000', 'Автоматични', 'Бензин',
             '306', '3000', '2012', 'Декември', '150000', '2/3', 'Сив', 'EURO 4', None, paths)
