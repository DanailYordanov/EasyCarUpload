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
        self.browser.get(
            "https://www.cars.bg/loginpage.php?ref=https://www.cars.bg/carslist.php?open_menu=1")
        time.sleep(1)

        phone_number = config('CARS_PHONE_NUMBER')
        password = config('CARS_PASSWORD')

        input = self.browser.find_element_by_xpath('//*[@id="phone"]')
        input.send_keys(phone_number)

        time.sleep(1)

        input = self.browser.find_element_by_xpath(
            '//*[@id="private_login_conteiner"]/div[1]/div[2]/div/input')
        input.send_keys(password)

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

        time.sleep(1)

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

    def add(self):
        self.open_publish_page()

        # Choose condition

        condition_page = self.browser.find_element_by_xpath(
            '//*[@id="conditionwrapper"]')
        condition_page.click()

        time.sleep(0.5)

        condition = self.browser.find_element_by_xpath(
            "//label[text()='В добро състояние']")
        condition.click()

        time.sleep(0.5)

        # Choose category

        category_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[7]')
        category_page.click()

        time.sleep(0.5)

        category = self.browser.find_element_by_xpath(
            "//label[text()='Седан']")
        category.click()

        time.sleep(0.5)

        # Choose brand and model

        brands_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[5]')
        brands_page.click()

        time.sleep(0.5)

        brand = self.browser.find_element_by_xpath("//label[text()='BMW']")
        brand.click()

        time.sleep(0.5)

        model = self.browser.find_element_by_xpath("//label[text()='335']")
        model.click()

        time.sleep(0.5)

        # Input engine type

        engine_input = self.browser.find_element_by_id('engine')
        engine_input.send_keys('335I N54')

        time.sleep(0.5)

        # Input price

        price_input = self.browser.find_element_by_id('price')
        price_input.send_keys('15000')

        time.sleep(0.5)

        # Choose gear

        gear_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[10]')
        gear_page.click()

        time.sleep(0.5)

        gears = self.browser.find_element_by_xpath(
            "//label[text()='Автоматични']")
        gears.click()

        time.sleep(0.5)

        # Choose fuel

        fuel_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[11]')
        fuel_page.click()

        time.sleep(0.5)

        fuel = self.browser.find_element_by_xpath("//label[text()='Бензин']")
        fuel.click()

        time.sleep(0.5)

        # Input power

        power_input = self.browser.find_element_by_id('power')
        power_input.send_keys('306')

        time.sleep(0.5)

        # Input cubature

        cubature_input = self.browser.find_element_by_id('cubature')
        cubature_input.send_keys('3000')

        time.sleep(0.5)

        # Choose year

        year_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[14]')
        year_page.click()

        time.sleep(0.5)

        year = self.browser.find_element_by_xpath("//label[text()='2012']")
        year.click()

        time.sleep(0.5)

        month = self.browser.find_element_by_xpath(
            "//label[text()='Декември']")
        month.click()

        time.sleep(0.5)

        # Input run

        run_input = self.browser.find_element_by_id('run')
        run_input.send_keys('130000')

        time.sleep(0.5)

        # Choose doors

        doors_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[16]')
        doors_page.click()

        time.sleep(0.5)

        doors = self.browser.find_element_by_xpath("//label[text()='2/3']")
        doors.click()

        time.sleep(0.5)

        # Choose color

        colors_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[17]')
        colors_page.click()

        time.sleep(0.5)

        color = self.browser.find_element_by_xpath("//label[text()='Сив']")
        color.click()

        time.sleep(0.5)

        self.browser.execute_script('closePublishSubPage($(this));')

        time.sleep(0.5)

        # Choose location

        location_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[19]')
        location_page.click()

        time.sleep(0.5)

        location = self.browser.find_element_by_xpath(
            "//label[text()='в България']")
        location.click()

        time.sleep(0.5)

        # Choose usage

        usage = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[20]/label')
        usage.click()

        time.sleep(0.5)

        # Choose euro

        euro_page = self.browser.find_element_by_xpath(
            '//*[@id="mainForm"]/ul/li[18]')
        euro_page.click()

        time.sleep(0.5)

        euro = self.browser.find_element_by_xpath("//label[text()='EURO 4']")
        euro.click()

        time.sleep(0.5)

        # Input description

        description = self.browser.find_element_by_id('notes')
        description.send_keys('Колата е перфектна')

        time.sleep(0.5)

        # # Upload images

        # paths = [
        #     'E:\Coding\CarsUpload\CarsUpload\pics\pic1.jpg',
        #     'E:\Coding\CarsUpload\CarsUpload\pics\pic2.jpg',
        #     'E:\Coding\CarsUpload\CarsUpload\pics\pic3.jpg',
        #     'E:\Coding\CarsUpload\CarsUpload\pics\pic4.jpg',
        #     'E:\Coding\CarsUpload\CarsUpload\pics\pic5.jpg',
        #     'E:\Coding\CarsUpload\CarsUpload\pics\pic6.jpg'
        # ]

        # i = 1
        # for path in paths:
        #     image_input = self.browser.find_element_by_id(
        #         'uploadFile' + str(i))
        #     image_input.send_keys(path)
        #     i += 1
        #     time.sleep(3)

        # time.sleep(0.5)

        # Click publish button

        button = self.browser.find_element_by_id('publishBtn')
        button.click()


instance = CarsBgClass()
instance.add()
