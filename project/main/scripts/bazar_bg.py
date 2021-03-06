from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from .options import options


class images_uploaded():
    """An expectation for checking that all images are uploaded"""

    def __init__(self, images_number):
        self.images_number = images_number

    def __call__(self, driver):
        images = driver.find_elements_by_xpath(
            '//div[@data-name]')
        if len(images) == self.images_number:
            return images
        else:
            return False


class BazarBgClass():

    def __init__(self):
        self.browser = webdriver.Firefox(
            options=options, executable_path=GeckoDriverManager().install())
        self.browser.implicitly_wait(30)
        self.login()

    def login(self):
        try:
            self.browser.get('https://bazar.bg/user/login')

            cookie_consent_button = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'fc-cta-consent')))
            cookie_consent_button.click()

            email = config('BAZAR_BG_EMAIL')
            password = config('BAZAR_BG_PASSWORD')

            email_input = WebDriverWait(self.browser, 30).until(
                EC.visibility_of_element_located((By.NAME, 'email')))
            email_input.send_keys(email)

            password_input = WebDriverWait(self.browser, 30).until(
                EC.visibility_of_element_located((By.NAME, 'password')))
            password_input.send_keys(password)

            button = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'loginSubmit')))
            button.click()

            # Wait for the authentication to complete
            WebDriverWait(self.browser, 30).until(
                EC.presence_of_element_located((By.ID, 'unreadMsg')))
        except BaseException as e:
            print(f'Something went wrong while logging you in! - {e}')

    def input_title(self, input):
        try:
            title_input = self.browser.find_element_by_name(
                'title')
            title_input.send_keys(input)
        except BaseException as e:
            print(
                f'Something went wrong while inputting a title ! - {e}')

    def choose_listing_type(self):
        try:
            listing_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.ID, 'rubChooser')))
            listing_select.click()

            choice = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'avto')))
            choice.click()
        except BaseException as e:
            print(
                f'Something went wrong while choosing a listing type ! - {e}')

    def choose_brand(self, choice):
        try:
            brand_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'brand')))
            brand_select = Select(brand_select)
            brand_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a brand ! - {e}')

    def choose_model(self, choice):
        try:
            model_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'model')))
            model_select = Select(model_select)
            model_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a model ! - {e}')

    def choose_fuel_type(self, choice):
        if choice == '????????????':
            choice = '????????????????'
        elif choice == '??????????':
            choice = '??????????????'
        elif choice == '????????????':
            choice = '????????????????'
        elif choice == '??????????????????????????':
            choice = '????????????????????????'

        try:
            fuel_type_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'engine')))
            fuel_type_select = Select(fuel_type_select)
            fuel_type_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a fuel type ! - {e}')

    def choose_transmission_type(self, choice):
        if choice == '??????????????????????':
            choice = '??????????????????????'
        elif choice == '??????????':
            choice = '??????????'

        try:
            transmission_type_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'transmission')))
            transmission_type_select = Select(transmission_type_select)
            transmission_type_select.select_by_visible_text(choice)
        except BaseException as e:
            print(
                f'Something went wrong while choosing a transmission type! - {e}')

    def choose_category(self, choice):
        try:
            category_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'vehicle_type')))
            category_select = Select(category_select)
            category_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a category ! - {e}')

    def choose_year(self, choice):
        try:
            year_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'year')))
            year_select = Select(year_select)
            year_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a year ! - {e}')

    def input_run(self, input):
        try:
            run_input = self.browser.find_element_by_name('mileage')
            run_input.send_keys(input)
        except BaseException as e:
            print(f'Something went wrong while inputting run ! - {e}')

    def input_price(self, input):
        try:
            price_type_button = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.ID, 'rprice2')))
            price_type_button.click()

            price_input = self.browser.find_element_by_name('price')
            price_input.send_keys(input)
        except BaseException as e:
            print(f'Something went wrong while inputting a price ! - {e}')

    def choose_condition(self):
        try:
            condition_button = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@name="condition" and @value="2"]')))
            condition_button.click()
        except BaseException as e:
            print(f'Something went wrong while choosing a condition ! - {e}')

    def input_description(self, input):
        try:
            self.browser.execute_script(
                f""" $("#redactorIframe").contents().find('body div')[0].innerText = "{input}" """)
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
                images_uploaded(len(paths)))
        except BaseException as e:
            print(f'Something went wrong while uploading images ! - {e}')

    def choose_location(self):
        try:
            region_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.ID, 'province_city_location')))
            region_select = Select(region_select)
            region_select.select_by_visible_text('???????????? ??????????????????')

            city_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.ID, 'populated_location')))
            city_select = Select(city_select)
            city_select.select_by_visible_text('????. ??????????????')
        except BaseException as e:
            print(f'Something went wrong while choosing a location ! - {e}')

    def input_phone_number(self, input):
        try:
            phone_number_input = self.browser.find_element_by_name('phone')
            phone_number_input.send_keys(input)

            hide_phone_button = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'hide_phone')))
            hide_phone_button.click()
        except BaseException as e:
            print(
                f'Something went wrong while inputting a phone number ! - {e}')

    def publish(self, category, brand, model, modification, price,
                transmission_type, fuel_type, year, run, description, image_paths, phone_number):
        try:
            self.browser.get('https://bazar.bg/ads/save')

            translator = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'translator')))
            translator.click()
            translator.click()

            self.input_title(f'{brand} {modification}')

            self.choose_listing_type()

            self.choose_brand(brand)

            self.choose_model(model)

            self.choose_fuel_type(fuel_type)

            self.choose_transmission_type(transmission_type)

            self.choose_category(category)

            self.choose_year(year)

            self.input_run(run)

            self.choose_condition()

            self.input_price(price)

            self.input_description(description)

            self.upload_images(image_paths)

            self.choose_location()

            self.input_phone_number(phone_number)

            button = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.ID, 'submitBtn')))
            button.click()

            offer_id = self.get_offer_id()

            return offer_id
        except BaseException as e:
            print(f'Something went wrong while publishing the offer ! - {e}')
        finally:
            self.browser.quit()

    def delete(self, offer_id):
        try:
            self.browser.get(
                f'https://bazar.bg/ads/archive/{offer_id}/')

            self.browser.get(f'https://bazar.bg/obiava-{offer_id}/')

            self.browser.find_element_by_class_name('blueBox')
        except BaseException as e:
            print(f'Something went wrong while deleting the offer ! - {e}')
        finally:
            self.browser.quit()

    def get_offer_id(self):
        try:
            # Wait for the offer details page to load

            WebDriverWait(self.browser, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'promotirane')))

            url = self.browser.current_url
            offer_id = url.split('/')[-1]
            offer_id = offer_id.split('?')[0]

            return offer_id
        except BaseException as e:
            print(f'Something went wrong while getting the offer id ! - {e}')
