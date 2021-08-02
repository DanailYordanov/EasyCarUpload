import os
import pickle
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class images_uploaded():
    """An expectation for checking that all images are uploaded"""

    def __init__(self, locator, images_number):
        self.locator = locator
        self.images_number = images_number

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        images = element.find_elements_by_class_name('haspic')
        if len(images) == self.images_number:
            return element
        else:
            return False


class CarsBgClass():

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)
        self.load_cookies()

    def login(self):

        self.browser.get(
            'https://www.cars.bg/loginpage.php?ref=https://www.cars.bg/carslist.php?open_menu=1')

        try:
            phone_number = config('CARS_BG_PHONE_NUMBER')
            password = config('CARS_BG_PASSWORD')

            phone_input = WebDriverWait(self.browser, 30).until(
                EC.visibility_of_element_located((By.NAME, 'phone')))
            phone_input.send_keys(phone_number)

            password_input = WebDriverWait(self.browser, 30).until(
                EC.visibility_of_element_located((By.NAME, 'password_private')))
            password_input.send_keys(password)

            button = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="private_login_conteiner"]/div[3]/button/div')))
            button.click()

            WebDriverWait(self.browser, 30).until(
                EC.presence_of_element_located((By.XPATH, '//a[@href="https://www.cars.bg/logout.php"]')))

            pickle.dump(self.browser.get_cookies(),
                        open("cars_bg_cookies.pkl", "wb"))
        except BaseException as e:
            print(f'Something went wrong while logging you in! - {e}')

    def load_cookies(self):
        try:
            self.browser.get('https://www.cars.bg/')
            cookies = pickle.load(open('cars_bg_cookies.pkl', 'rb'))

            for cookie in cookies:
                self.browser.add_cookie(cookie)

            self.browser.refresh()
        except Exception:
            self.login()

    def open_publish_page(self):
        self.browser.get('https://www.cars.bg/publish.php')

        element = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mainForm"]/ul/li/a')))
        element.click()

        element = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div/ul/li[2]/label')))
        element.click()

        element = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/main/div/form/ul/li[2]/label')))
        element.click()

    def choose_condition(self):
        try:
            condition_page = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@sync-data="conditionSelectPage"]')))
            condition_page.click()

            condition_choice = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//label[text()='В добро състояние']")))
            condition_choice.click()
        except BaseException as e:
            print(f'Something went wrong while choosing condition ! - {e}')

    def choose_category(self, choice):
        try:
            category_page = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@sync-data="categorySelectPage"]')))
            category_page.click()

            category_choice = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, f"//label[text()='{choice}']")))
            category_choice.click()
        except BaseException as e:
            print(f'Something went wrong while choosing a category ! - {e}')

    def choose_brand(self, choice):
        try:
            brands_page = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@sync-data="brandSelectPage"]')))
            brands_page.click()

            brand_choice = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, f"//label[text()='{choice}']")))
            brand_choice.click()
        except BaseException as e:
            print(f'Something went wrong while choosing a brand ! - {e}')

    def choose_model(self, choice):
        try:
            model_choice = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, f"//label[text()='{choice}']")))
            model_choice.click()
        except BaseException as e:
            print(f'Something went wrong while choosing a model ! - {e}')

    def input_modification(self, input):
        if input:
            try:
                modification_input = self.browser.find_element_by_id('engine')
                modification_input.send_keys(input)
            except BaseException as e:
                print(
                    f'Something went wrong while inputting a modification ! - {e}')

    def input_price(self, input):
        try:
            price_input = self.browser.find_element_by_id('price')
            price_input.send_keys(input)
        except BaseException as e:
            print(f'Something went wrong while inputting a price ! - {e}')

    def choose_transmission_type(self, choice):
        try:
            transmission_page = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@sync-data="gearSelectPage"]')))
            transmission_page.click()

            transmission_choice = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, f"//label[text()='{choice}']")))
            transmission_choice.click()
        except BaseException as e:
            print(
                f'Something went wrong while choosing a transmission type ! - {e}')

    def choose_fuel_type(self, choice):
        try:
            fuel_page = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@sync-data="fuelSelectPage"]')))
            fuel_page.click()

            fuel_choice = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, f"//label[text()='{choice}']")))
            fuel_choice.click()
        except BaseException as e:
            print(f'Something went wrong while choosing a fuel type ! - {e}')

    def input_power(self, input):
        if input:
            try:
                power_input = self.browser.find_element_by_id('power')
                power_input.send_keys(input)
            except BaseException as e:
                print(f'Something went wrong while inputting power ! - {e}')

    def input_displacement(self, input):
        if input:
            try:
                cubature_input = self.browser.find_element_by_id('cubature')
                cubature_input.send_keys(input)
            except BaseException as e:
                print(
                    f'Something went wrong while inputting displacement ! - {e}')

    def choose_year_and_month(self, year_choice, month_choice):
        try:
            year_page = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@sync-data="yearSelectPage"]')))
            year_page.click()

            year_choice = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, f"//label[text()='{year_choice}']")))
            year_choice.click()

            month_choice = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, f"//label[text()='{month_choice}']")))
            month_choice.click()
        except BaseException as e:
            print(
                f'Something went wrong while choosing an year and a month ! - {e}')

    def input_run(self, input):
        try:
            run_input = self.browser.find_element_by_id('run')
            run_input.send_keys(input)
        except BaseException as e:
            print(f'Something went wrong while inputting run ! - {e}')

    def choose_doors_type(self, choice):
        try:
            doors_page = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@sync-data="doorsSelectPage"]')))
            doors_page.click()

            doors_choice = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, f"//label[text()='{choice}']")))
            doors_choice.click()
        except BaseException as e:
            print(f'Something went wrong while choosing a doors type ! - {e}')

    def choose_color(self, choice):
        try:
            colors_page = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@sync-data="colorSelectPage"]')))
            colors_page.click()

            color_choice = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, f"//label[text()='{choice}']")))
            color_choice.click()

            back_button = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[17]/header/div/section[1]/button')))
            back_button.click()

        except BaseException as e:
            print(f'Something went wrong while choosing a color ! - {e}')

    def choose_location(self, choice):
        try:
            location_page = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@sync-data="isbgSelectPage"]')))
            location_page.click()

            location_choice = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, f"//label[text()='{choice}']")))
            location_choice.click()
        except BaseException as e:
            print(f'Something went wrong while choosing a location ! - {e}')

    def choose_usage(self):
        try:
            usage = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//label[@for="usageId"]')))
            usage.click()
        except BaseException as e:
            print(f'Something went wrong while choosing usage ! - {e}')

    def choose_euro_standart(self, choice):
        if choice:
            try:
                euro_standart_page = WebDriverWait(self.browser, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//a[@sync-data="euroSelectPage"]')))
                euro_standart_page.click()

                euro_standart_choice = WebDriverWait(self.browser, 30).until(
                    EC.element_to_be_clickable((By.XPATH, f"//label[text()='{choice}']")))
                euro_standart_choice.click()
            except BaseException as e:
                print(
                    f'Something went wrong while choosing a EURO standart ! - {e}')

    def input_description(self, input):
        if input:
            try:
                description = self.browser.find_element_by_id('notes')
                description.send_keys(input)
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
                images_uploaded((By.ID, 'sortable'), len(paths)))
        except BaseException as e:
            print(f'Something went wrong while uploading images ! - {e}')

    def publish(self, category, brand, model, modification, price,
                transmission_type, fuel_type, power, displacement, year, month, run,
                doors_type, color, euro_standart, description, image_paths):

        self.open_publish_page()

        self.choose_condition()

        self.choose_brand(brand)

        self.choose_model(model)

        self.input_modification(modification)

        self.choose_category(category)

        self.input_price(price)

        self.choose_transmission_type(transmission_type)

        self.choose_fuel_type(fuel_type)

        self.input_power(power)

        self.input_displacement(displacement)

        self.choose_year_and_month(year, month)

        self.input_run(run)

        self.choose_doors_type(doors_type)

        self.choose_color(color)

        self.choose_euro_standart(euro_standart)

        self.choose_location('в България')

        self.choose_usage()

        self.input_description(description)

        self.upload_images(image_paths)

        button = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.ID, 'publishBtn')))
        button.click()

        offer_id = self.get_offer_id()

        self.browser.quit()

        return offer_id

    def delete(self, offer_id):

        self.browser.get(
            f'https://www.cars.bg/offer/{offer_id}?myoffer=1')

        delete_button = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-action="openDeleteoffer"]')))
        delete_button.click()

        confirm_delete_button = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-action="deleteofferCloseYes"]')))
        confirm_delete_button.click()

    def get_offer_id(self):

        # Wait for the offer details page to load

        WebDriverWait(self.browser, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'description')))

        url = self.browser.current_url
        offer_id = url.split('/')[-1]
        offer_id = offer_id.split('?')[0]

        return offer_id
