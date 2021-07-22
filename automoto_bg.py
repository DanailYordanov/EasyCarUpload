import os
import time
import pickle
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class images_uploaded():
    """An expectation for checking that all images are uploaded"""

    def __init__(self, locator, images_number):
        self.locator = locator
        self.images_number = images_number

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        images = element.find_elements_by_xpath('.//div[string-length(@id)>0]')
        if len(images) == self.images_number:
            return element
        else:
            return False


class AutomotoBg():

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)
        self.load_cookies()

    def login(self):

        self.browser.get('https://automoto.bg/login')

        try:
            cookie_consent_button = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'cc-btn')))
            cookie_consent_button.click()

            email = config('AUTOMOTO_BG_EMAIL')
            password = config('AUTOMOTO_BG_PASSWORD')

            email_input = self.browser.find_element_by_name('email')
            email_input.send_keys(email)

            password_input = self.browser.find_element_by_name('password')
            password_input.send_keys(password)

            WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/section/form/div[2]/label/button')))

            self.browser.execute_script(
                """$('button[type="submit"]').click();""")

            time.sleep(5)

            pickle.dump(self.browser.get_cookies(),
                        open('automoto_bg_cookies.pkl', 'wb'))
        except BaseException as e:
            print(f'Something went wrong while logging you in ! - {e}')

    def load_cookies(self):
        try:
            self.browser.get('https://automoto.bg/')
            cookies = pickle.load(open('automoto_bg_cookies.pkl', 'rb'))

            for cookie in cookies:
                self.browser.add_cookie(cookie)

            self.browser.refresh()
        except:
            self.login()

    def choose_brand(self, choice):
        try:
            brand_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'mark_id')))
            brand_select = Select(brand_select)
            brand_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a brand ! - {e}')

    def choose_model(self, choice):
        try:
            model_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'model_id')))
            model_select = Select(model_select)
            model_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a model ! - {e}')

    def input_modification(self, input):
        try:
            modification_input = self.browser.find_element_by_name(
                'modification')
            modification_input.send_keys(input)
        except BaseException as e:
            print(
                f'Something went wrong while inputting a modification ! - {e}')

    def choose_category(self, choice):
        try:
            category_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'coupe_id')))
            category_select = Select(category_select)
            category_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a category ! - {e}')

    def input_price(self, input):
        try:
            price_input = self.browser.find_element_by_name('price')
            price_input.send_keys(input)
        except BaseException as e:
            print(f'Something went wrong while inputting a price ! - {e}')

    def choose_transmission_type(self, choice):
        try:
            transmission_type_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'speed_id')))
            transmission_type_select = Select(
                self.browser.find_element_by_name('speed_id'))
            transmission_type_select.select_by_visible_text(choice)
        except BaseException as e:
            print(
                f'Something went wrong while choosing a transmission type! - {e}')

    def choose_fuel_type(self, choice):
        try:
            fuel_type_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'fuel_id')))
            fuel_type_select = Select(
                self.browser.find_element_by_name('fuel_id'))
            fuel_type_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a fuel type ! - {e}')

    def input_power(self, input):
        try:
            power_input = self.browser.find_element_by_name('power')
            power_input.send_keys(input)
        except BaseException as e:
            print(f'Something went wrong while inputting power ! - {e}')

    def input_displacement(self, input):
        try:
            displacement_input = self.browser.find_element_by_name('cubic')
            displacement_input.send_keys(input)
        except BaseException as e:
            print(f'Something went wrong while inputting displacement ! - {e}')

    def choose_month(self, choice):
        try:
            month_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'month_id')))
            month_select = Select(
                self.browser.find_element_by_name('month_id'))
            month_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a month ! - {e}')

    def choose_year(self, choice):
        try:
            year_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'year_id')))
            year_select = Select(self.browser.find_element_by_name('year_id'))
            year_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a year ! - {e}')

    def input_run(self, input):
        try:
            run_input = self.browser.find_element_by_name('mileage')
            run_input.send_keys(input)
        except BaseException as e:
            print(f'Something went wrong while inputting run ! - {e}')

    def choose_doors_type(self, choice):
        try:
            doors_type_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'door_id')))
            doors_type_select = Select(
                self.browser.find_element_by_name('door_id'))
            doors_type_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a doors type ! - {e}')

    def choose_color(self, choice):
        try:
            color_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'color_id')))
            color_select = Select(
                self.browser.find_element_by_name('color_id'))
            color_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a color ! - {e}')

    def choose_euro_standart(self, choice):
        try:
            euro_standart_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'euro_standart_id')))
            euro_standart_select = Select(
                self.browser.find_element_by_name('euro_standart_id'))
            euro_standart_select.select_by_visible_text(choice)
        except BaseException as e:
            print(
                f'Something went wrong while choosing a EURO standart ! - {e}')

    def input_description(self, input):
        try:
            description_input = self.browser.find_element_by_id('description')
            description_input.send_keys(input)
        except BaseException as e:
            print(
                f'Something went wrong while inputting a description ! - {e}')

    def upload_images(self, paths):
        try:
            # When you join all paths with \n you can pass them to the input at once

            multiple_images_path = '\n'.join(paths)
            image_input = self.browser.find_element_by_xpath(
                '//input[@type="file"]')
            image_input.send_keys(multiple_images_path)

            # Wait for the images to upload

            WebDriverWait(self.browser, 30).until(
                images_uploaded((By.ID, 'images'), len(paths)))
        except BaseException as e:
            print(f'Something went wrong while uploading images ! - {e}')

    def publish(self, category, brand, model, modification, price,
                transmission_type, fuel_type, power, displacement, year, month, run,
                doors_type, color, euro_standart, description, image_paths):

        self.browser.get('https://automoto.bg/listings/create')

        self.choose_brand(brand)

        self.choose_model(model)

        self.input_modification(modification)

        self.choose_category(category)

        self.input_price(price)

        self.choose_transmission_type(transmission_type)

        self.choose_fuel_type(fuel_type)

        self.input_power(power)

        self.input_displacement(displacement)

        self.choose_month(month)

        self.choose_year(year)

        self.input_run(run)

        self.choose_doors_type(doors_type)

        self.choose_color(color)

        self.choose_euro_standart(euro_standart)

        self.input_description(description)

        self.upload_images(image_paths)

        button = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="ID-listingOnlyCarCreate"]/div[24]/div/button')))
        button.click()

    def delete(self, offer_id):
        self.browser.get(
            f'https://automoto.bg/profile/delete-listing/{offer_id}')


BASE_DIR = os.path.dirname(__file__)

paths = [
    os.path.join(BASE_DIR, '..\pics\pic1.jpg'),
    os.path.join(BASE_DIR, '..\pics\pic2.jpg'),
    os.path.join(BASE_DIR, '..\pics\pic3.jpg'),
    os.path.join(BASE_DIR, '..\pics\pic4.jpg'),
    os.path.join(BASE_DIR, '..\pics\pic5.jpg'),
    os.path.join(BASE_DIR, '..\pics\pic6.jpg')
]

instance = AutomotoBg()
instance.publish('Седан', 'BMW', '335', '335i', '20000', 'Автоматични', 'Бензин',
                 '306', '3000', '2012', 'Декември', '150000', '2/3', 'Сив', 'EURO 4', 'Колата е перфектна', paths)
