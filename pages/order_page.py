import allure
from locators.order_page_locators import *


class FormOrder:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполнить первую форму заказа')
    def fill_first_form(self, name, surname, addres, station, phone):
        self.driver.find_element(*FirstForm.name).send_keys(name)
        self.driver.find_element(*FirstForm.surname).send_keys(surname)
        self.driver.find_element(*FirstForm.addres).send_keys(addres)
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

