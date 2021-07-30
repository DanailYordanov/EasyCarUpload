import os
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


class Car24BgClass():

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

    def choose_brand(self, choice):
        try:
            brand_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'f4')))
            brand_select = Select(brand_select)
            brand_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a brand ! - {e}')

    def choose_model(self, choice):
        try:
            model_select = WebDriverWait(self.browser, 30).until(
                options_present((By.NAME, 'f5')))
            model_select = Select(model_select)
            model_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a model ! - {e}')

    def input_modification(self, input):
        if input:
            try:
                modification_input = self.browser.find_element_by_name(
                    'f6')
                modification_input.send_keys(input)
            except BaseException as e:
                print(
                    f'Something went wrong while inputting a modification ! - {e}')

    def choose_category(self, choice):
        try:
            category_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'f10')))
            category_select = Select(category_select)
            category_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a category ! - {e}')

    def input_price(self, input):
        try:
            price_input = self.browser.find_element_by_name('f11')
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
                EC.element_to_be_clickable((By.NAME, 'f9')))
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
                EC.element_to_be_clickable((By.NAME, 'f7')))
            fuel_type_select = Select(fuel_type_select)
            fuel_type_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a fuel type ! - {e}')

    def input_power(self, input):
        if input:
            try:
                power_input = self.browser.find_element_by_name('f8')
                power_input.send_keys(input)
            except BaseException as e:
                print(f'Something went wrong while inputting power ! - {e}')

    def choose_month(self, choice):
        try:
            month_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'f13')))
            month_select = Select(month_select)
            month_select.select_by_visible_text(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a month ! - {e}')

    def choose_year(self, choice):
        try:
            year_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'f14')))
            year_select = Select(year_select)
            year_select.select_by_value(choice)
        except BaseException as e:
            print(f'Something went wrong while choosing a year ! - {e}')

    def input_run(self, input):
        try:
            run_input = self.browser.find_element_by_name('f15')
            run_input.send_keys(input)
        except BaseException as e:
            print(f'Something went wrong while inputting run ! - {e}')

    def choose_color(self, choice):
        if choice:
            try:
                color_select = WebDriverWait(self.browser, 30).until(
                    EC.element_to_be_clickable((By.NAME, 'f16')))
                color_select = Select(color_select)
                color_select.select_by_visible_text(choice)
            except BaseException as e:
                print(f'Something went wrong while choosing a color ! - {e}')

    def input_description(self, input):
        if input:
            try:
                description_input = self.browser.find_element_by_name('f19')
                description_input.send_keys(input)
            except BaseException as e:
                print(
                    f'Something went wrong while inputting a description ! - {e}')

    def choose_region(self, choice):
        try:
            region_select = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.NAME, 'f17')))
            region_select = Select(region_select)
            region_select.select_by_visible_text(choice)
        except BaseException as e:
            print(
                f'Something went wrong while choosing a region ! - {e}')

    def input_phone_number(self, input):
        try:
            phone_number_input = self.browser.find_element_by_name('f20')
            phone_number_input.send_keys(input)
        except BaseException as e:
            print(
                f'Something went wrong while inputting a phone number ! - {e}')

    def input_email_address(self, input):
        try:
            email_address_input = self.browser.find_element_by_name('f21')
            email_address_input.send_keys(input)
        except BaseException as e:
            print(
                f'Something went wrong while inputting an email address ! - {e}')

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
                color, description, image_paths, phone_number, email_address):

        self.browser.get(
            'https://www.car24.bg/pcgi/car.cgi?act=5')

        self.choose_brand(brand)

        self.choose_model(model)

        self.input_modification(modification)

        self.choose_fuel_type(fuel_type)

        self.input_power(power)

        self.choose_transmission_type(transmission_type)

        self.choose_category(category)

        self.input_price(price)

        self.choose_month(month)

        self.choose_year(year)

        self.input_run(run)

        self.choose_color(color)

        self.input_description(description)

        self.choose_region('Дупница')

        self.input_phone_number(phone_number)

        self.input_email_address(email_address)

        # Click the TOS checkbox with JS

        self.browser.execute_script(
            """document.getElementsByName('chkcond')[0].click();""")

        button = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'button')))
        button.click()

        add_photos_button = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'button')))
        add_photos_button.click()

        self.upload_images(image_paths)

        publish_button = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'button')))
        publish_button.click()
