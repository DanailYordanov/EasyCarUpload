from selenium import webdriver
from selenium.webdriver.support.ui import Select
from decouple import config
import time
import pickle


class AutoBgClass():

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.load_cookies()

    def load_cookies(self):
        try:
            self.browser.get("https://www.auto.bg/")
            cookies = pickle.load(open("auto_bg_cookies.pkl", "rb"))

            for cookie in cookies:
                self.browser.add_cookie(cookie)

            time.sleep(1)

            self.browser.refresh()

            time.sleep(1)

        except Exception:
            self.login()

    def login(self):
        email = config('AUTO_BG_EMAIL')
        password = config('AUTO_BG_PASSWORD')

        self.browser.get('https://www.auto.bg/login')

        time.sleep(1)

        consent_button = self.browser.find_element_by_class_name(
            'fc-cta-consent')
        consent_button.click()

        time.sleep(0.5)

        email_input = self.browser.find_element_by_name('email_phone')
        email_input.send_keys(email)

        time.sleep(0.5)

        password_input = self.browser.find_element_by_name('passw')
        password_input.send_keys(password)

        time.sleep(0.5)

        login_button = self.browser.find_element_by_xpath(
            '//*[@id="loginLeft"]/div/ul/form/li[11]/button')
        login_button.click()

        pickle.dump(self.browser.get_cookies(),
                    open("auto_bg_cookies.pkl", "wb"))

    def publish(self):

        self.browser.get('https://www.auto.bg/newoffer')

        time.sleep(1)

        category = Select(self.browser.find_element_by_name('category'))
        category.select_by_visible_text('Седан')

        time.sleep(0.5)

        brand = Select(self.browser.find_element_by_name('marka'))
        brand.select_by_visible_text('BMW')

        time.sleep(0.5)

        model = Select(self.browser.find_element_by_name('model'))
        model.select_by_visible_text('335')

        time.sleep(0.5)

        condition = self.browser.find_element_by_xpath(
            '//*[@id="searchBoxPage"]/li[3]/div[2]/label[1]/input')
        condition.click()

        time.sleep(0.5)

        price = self.browser.find_element_by_name('price')
        price.send_keys('20000')

        time.sleep(0.5)

        fuel_type = Select(self.browser.find_element_by_name('engine_type'))
        fuel_type.select_by_visible_text('Бензин')

        time.sleep(0.5)

        gear_type = Select(self.browser.find_element_by_name('transmission'))
        gear_type.select_by_visible_text('Автоматична')

        time.sleep(0.5)

        power = self.browser.find_element_by_name('engine_power')
        power.send_keys('306')

        time.sleep(0.5)

        run = self.browser.find_element_by_name('km')
        run.send_keys('150000')

        time.sleep(0.5)

        engine_type = self.browser.find_element_by_name('modification')
        engine_type.send_keys('335i')

        time.sleep(0.5)

        month = Select(self.browser.find_element_by_name('month'))
        month.select_by_visible_text('декември')

        time.sleep(0.5)

        year = Select(self.browser.find_element_by_name('year'))
        year.select_by_visible_text('2012')

        time.sleep(0.5)

        location = Select(self.browser.find_element_by_name('locat'))
        location.select_by_visible_text('Дупница')

        time.sleep(0.5)

        dealership_location = Select(
            self.browser.find_element_by_name('locatc'))
        dealership_location.select_by_visible_text('с. Блатино')

        time.sleep(0.5)

        color = Select(self.browser.find_element_by_name('color'))
        color.select_by_visible_text('Сив')

        time.sleep(0.5)

        paths = [
            'E:\Coding\CarsUpload\CarsUpload\pics\pic1.jpg',
            'E:\Coding\CarsUpload\CarsUpload\pics\pic2.jpg',
            'E:\Coding\CarsUpload\CarsUpload\pics\pic3.jpg',
            'E:\Coding\CarsUpload\CarsUpload\pics\pic4.jpg',
            'E:\Coding\CarsUpload\CarsUpload\pics\pic5.jpg',
            'E:\Coding\CarsUpload\CarsUpload\pics\pic6.jpg'
        ]

        for path in paths:
            image_input = self.browser.find_element_by_xpath(
                '//input[@type="file"]')
            image_input.send_keys(path)
            time.sleep(2)

        description = self.browser.find_element_by_name('extinfo')
        description.send_keys('Колата е перфектна')

        time.sleep(0.5)

        phone = self.browser.find_element_by_name('phone')
        phone.send_keys('0892216500')

        time.sleep(0.5)

        button = self.browser.find_element_by_name('subm')
        button.click()


instance = AutoBgClass()
instance.publish()
