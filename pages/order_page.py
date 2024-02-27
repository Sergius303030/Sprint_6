from pages.base_page import *
import allure
from locators.order_page_locators import *
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import *
from selenium.webdriver.support import expected_conditions as EC


class FormOrder:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)
        self.base_page = BasePage(self.driver)

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        self.base_page.click_cookie_accept()

    @allure.step('Клик по логотипу Самоката')
    def click_logo_scooter(self):
        self.base_page.click_logo_scooter()

    @allure.step('Клик по логотипу Яндекса')
    def click_logo_yandex(self):
        self.base_page.click_logo_yandex()

    @allure.step('Клик по верхней кнопке "Заказать"')
    def click_button_order_header(self):
        self.wait.until(EC.element_to_be_clickable(MainPage.button_order_header))
        self.driver.find_element(*MainPage.button_order_header).click()

    @allure.step('Клик по нижней кнопке "Заказать"')
    def click_button_order_bottom(self):
        self.driver.find_element(*MainPage.button_order_bottom).click()

    @allure.title('Заполнить всю форму заказа')
    def fill_full_order(self, firstname, surname, address, station, phone, date, rental_period, color, comment):
        self.firstname = firstname
        self.surname = surname
        self.address = address
        self.station = station
        self.phone = phone
        self.date = date
        self.rental_period = rental_period
        self.color = color
        self.comment = comment
        self.fill_first_form(name=self.firstname, surname=self.surname, address=self.address,
                                    station=self.station, phone=self.phone)
        self.fill_first_form_button_next()
        self.fill_second_form(date=self.date, index=self.rental_period, color=self.color, comment=self.comment)
        self.fill_second_form_button_next()
        self.button_yes_confirmation_window()


    @allure.step('Заполнить первую форму заказа')
    def fill_first_form(self, name, surname, address, station, phone):
        self.driver.find_element(*FirstForm.name).send_keys(name)
        self.driver.find_element(*FirstForm.surname).send_keys(surname)
        self.driver.find_element(*FirstForm.address).send_keys(address)
        self.driver.find_element(*FirstForm.station).click()
        self.driver.find_element(*FirstForm.station).send_keys(station)
        self.driver.find_element(*FirstForm.click_station).click()
        self.driver.find_element(*FirstForm.phone).send_keys(phone)

    @allure.step('Клик по кнопке "Далее"')
    def fill_first_form_button_next(self):
        self.driver.find_element(*FirstForm.button_next).click()

    @allure.step('Заполнить вторую форму заказа')
    def fill_second_form(self, date, index, color, comment):
        self.driver.find_element(*SecondForm.date).click()
        self.driver.find_element(*SecondForm.date).send_keys(date)
        self.driver.find_element(*SecondForm.dropdown).click()
        self.driver.find_elements(*SecondForm.dropdown_option)[index].click()
        self.driver.find_element(By.ID, color).click()
        self.driver.find_element(*SecondForm.comment).send_keys(comment)

    @allure.step('Клик по кнопке "Далее"')
    def fill_second_form_button_next(self):
        self.driver.find_element(*SecondForm.button_next).click()

    @allure.step('Клик по кнопке "Да"')
    def button_yes_confirmation_window(self):
        self.driver.find_element(*ModalWindow.button_confirm).click()

    @allure.step('Получить сообщение об успешном создании заказа')
    def get_order_text(self):
        text = self.driver.find_element(*ModalWindow.title).text
        return text

    @allure.step('Клик по кнопке "Проверить заказ"')
    def button_check_status_modal_window(self):
        self.driver.find_element(*ModalWindow.button_check_status).click()

