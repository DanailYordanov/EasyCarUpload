from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from decouple import config
import time
import pickle


class CarsBgClass():

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.load_cookies()

    def login(self):
        phone_number = config('CARS_PHONE_NUMBER')
        password = config('CARS_PASSWORD')

        self.browser.get(
            "https://www.cars.bg/loginpage.php?ref=https://www.cars.bg/carslist.php?open_menu=1")

        time.sleep(1)

        phone_input = self.browser.find_element_by_xpath('//*[@id="phone"]')
        phone_input.send_keys(phone_number)

        time.sleep(1)

        password_input = self.browser.find_element_by_xpath(
            '//*[@id="private_login_conteiner"]/div[1]/div[2]/div/input')
        password_input.send_keys(password)

        time.sleep(1)

        element = self.browser.find_element_by_xpath(
            '//*[@id="private_login_conteiner"]/div[3]/button/div')
        element.click()

        time.sleep(1)

        pickle.dump(self.browser.get_cookies(), open("cookies.pkl", "wb"))

    def load_cookies(self):
        try:
            self.browser.get("https://www.cars.bg/")
            cookies = pickle.load(open("cookies.pkl", "rb"))

            for cookie in cookies:
                self.browser.add_cookie(cookie)

            time.sleep(1)

            self.browser.refresh()

            time.sleep(1)

            self.browser.find_element_by_class_name('mdc-drawer__subtitle')

        except Exception:
            self.login()

    def open_publish_page(self):
        self.browser.get("https://www.cars.bg/publish.php")

        time.sleep(0.5)

        element = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li/a')
        element.click()

        time.sleep(0.5)

        element = self.browser.find_element_by_xpath(
            '//*[@id="main-content"]/div/ul/li[2]/label')
        element.click()

        time.sleep(1)

        self.browser.execute_script(
            'closePublishSubPage($(this));toggleCondition(2);')

    def export_brands(self):
        self.open_publish_page()

        element = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[5]')
        element.click()

        time.sleep(0.5)

        brands = self.browser.find_elements_by_tag_name('label')
        for brand in brands:
            if(brand.text != ''):

                print('=================================')
                print(brand.text)
                print('=================================')

                brand.click()

                time.sleep(0.5)

                i = 2
                while True:
                    try:
                        models = self.browser.find_element_by_xpath(
                            f'//*[@id="modelsconteiner"]/ul/li[{i}]')
                    except NoSuchElementException:
                        break
                    else:
                        print(models.text)
                        i += 1

                time.sleep(0.5)

                # Closes brand's models page
                self.browser.execute_script(
                    "$('.close-paged-select-publish').trigger('vclick')")

                time.sleep(0.5)

                element = self.browser.find_element_by_xpath(
                    '//*[@id="mainForm"]/ul/li[5]')
                element.click()

                time.sleep(0.5)

    def choose_condition(self):
        condition_page = self.browser.find_element_by_xpath(
            '//*[@id="conditionwrapper"]')
        condition_page.click()

        time.sleep(0.5)

        condition = self.browser.find_element_by_xpath(
            "//label[text()='В добро състояние']")
        condition.click()

    def choose_category(self, choice):
        category_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[7]')
        category_page.click()

        time.sleep(0.5)

        category = self.browser.find_element_by_xpath(
            f"//label[text()='{choice}']")
        category.click()

    def choose_brand(self, choice):
        brands_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[5]')
        brands_page.click()

        time.sleep(0.5)

        brand = self.browser.find_element_by_xpath(
            f"//label[text()='{choice}']")
        brand.click()

    def choose_model(self, choice):
        model = self.browser.find_element_by_xpath(
            f"//label[text()='{choice}']")
        model.click()

    def input_engine_type(self, input):
        engine_input = self.browser.find_element_by_id('engine')
        engine_input.send_keys(input)

    def input_price(self, input):
        price_input = self.browser.find_element_by_id('price')
        price_input.send_keys(input)

    def choose_gear_type(self, choice):
        gear_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[10]')
        gear_page.click()

        time.sleep(0.5)

        gears = self.browser.find_element_by_xpath(
            f"//label[text()='{choice}']")
        gears.click()

    def choose_fuel_type(self, choice):
        fuel_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[11]')
        fuel_page.click()

        time.sleep(0.5)

        fuel = self.browser.find_element_by_xpath(
            f"//label[text()='{choice}']")
        fuel.click()

    def input_power(self, input):
        power_input = self.browser.find_element_by_id('power')
        power_input.send_keys(input)

    def input_cubature(self, input):
        cubature_input = self.browser.find_element_by_id('cubature')
        cubature_input.send_keys(input)

    def choose_year_and_month(self, year_choice, month_choice):
        year_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[14]')
        year_page.click()

        time.sleep(0.5)

        year = self.browser.find_element_by_xpath(
            f"//label[text()='{year_choice}']")
        year.click()

        time.sleep(0.5)

        month = self.browser.find_element_by_xpath(
            f"//label[text()='{month_choice}']")
        month.click()

    def input_run(self, input):
        run_input = self.browser.find_element_by_id('run')
        run_input.send_keys(input)

    def choose_doors_type(self, choice):
        doors_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[16]')
        doors_page.click()

        time.sleep(0.5)

        doors = self.browser.find_element_by_xpath(
            f"//label[text()='{choice}']")
        doors.click()

    def choose_color(self, choice):
        colors_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[17]')
        colors_page.click()

        time.sleep(0.5)

        color = self.browser.find_element_by_xpath(
            f"//label[text()='{choice}']")
        color.click()

        time.sleep(0.5)

        self.browser.execute_script('closePublishSubPage($(this));')

    def choose_location(self, choice):
        location_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[19]')
        location_page.click()

        time.sleep(0.5)

        location = self.browser.find_element_by_xpath(
            f"//label[text()='{choice}']")
        location.click()

    def choose_usage(self):
        usage = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[20]/label')
        usage.click()

    def choose_euro_type(self, choice):
        euro_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[18]')
        euro_page.click()

        time.sleep(0.5)

        euro = self.browser.find_element_by_xpath(
            f"//label[text()='{choice}']")
        euro.click()

    def input_description(self, input):
        description = self.browser.find_element_by_id('notes')
        description.send_keys(input)

    def upload_images(self, paths):
        i = 1
        for path in paths:
            image_input = self.browser.find_element_by_id(
                'uploadFile' + str(i))
            image_input.send_keys(path)
            i += 1
            time.sleep(3)

    def add(self):
        self.open_publish_page()

        time.sleep(0.5)

        # Choose condition

        self.choose_condition()

        time.sleep(0.5)

        # Choose category

        self.choose_category('Седан')

        time.sleep(0.5)

        # Choose brand and model

        self.choose_brand('BMW')

        time.sleep(0.5)

        self.choose_model('335')

        time.sleep(0.5)

        # Input engine type

        self.input_engine_type('335I N54')

        time.sleep(0.5)

        # Input price

        self.input_price('15000')

        time.sleep(0.5)

        # Choose gear type

        self.choose_gear_type('Автоматични')

        time.sleep(0.5)

        # Choose fuel type

        self.choose_fuel_type('Бензин')

        time.sleep(0.5)

        # Input power

        self.input_power('306')

        time.sleep(0.5)

        # Input cubature

        self.input_cubature('3000')

        time.sleep(0.5)

        # Choose year and month

        self.choose_year_and_month('2012', 'Декември')

        time.sleep(0.5)

        # Input run

        self.input_run('130000')

        time.sleep(0.5)

        # Choose doors type

        self.choose_doors_type('2/3')

        time.sleep(0.5)

        # Choose color

        self.choose_color('Сив')

        time.sleep(0.5)

        # Choose location

        self.choose_location('в България')

        time.sleep(0.5)

        # Choose usage

        self.choose_usage()

        time.sleep(0.5)

        # Choose euro

        self.choose_euro_type('EURO 4')

        time.sleep(0.5)

        # Input description

        self.input_description('Колата е перфектна')

        time.sleep(0.5)

        # Upload images

        paths = [
            'E:\Coding\CarsUpload\CarsUpload\pics\pic1.jpg',
            'E:\Coding\CarsUpload\CarsUpload\pics\pic2.jpg',
            'E:\Coding\CarsUpload\CarsUpload\pics\pic3.jpg',
            'E:\Coding\CarsUpload\CarsUpload\pics\pic4.jpg',
            'E:\Coding\CarsUpload\CarsUpload\pics\pic5.jpg',
            'E:\Coding\CarsUpload\CarsUpload\pics\pic6.jpg'
        ]

        self.upload_images(paths)

        time.sleep(0.5)

        # Click publish button

        button = self.browser.find_element_by_id('publishBtn')
        button.click()


instance = CarsBgClass()
instance.add()
