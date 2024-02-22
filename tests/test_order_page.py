import allure
import pytest
from pages.order_page import FormOrder
from pages.base_page import BasePage
from locators.order_page_locators import FirstForm
from conftest import *
from parametrize.parametrize import UserData


class TestFormOrder:
    @allure.title('Проверка успешного сценария создания заказа')
    @pytest.mark.parametrize('firstname, surname, address, station, phone, date, rental_period, color, comment', UserData.data_user)
    def test_order_succsess(self, firstname, surname, address, station, phone, date, rental_period, color, comment, driver):
        self.driver = driver
        self.bp = BasePage(self.driver)
        self.fo = FormOrder(self.driver)
        self.bp.click_cookie_accept()
        self.bp.click_button_order_header()
        self.firstname = firstname
        self.surname = surname
        self.address = address
        self.station = station
        self.phone = phone
        self.date = date
        self.rental_period = rental_period
        self.color = color
        self.comment = comment
        self.fo.fill_first_form(name=self.firstname, surname=self.surname, addres=self.address,
                           station=self.station, phone=self.phone)
        self.fo.fill_first_form_button_next()
        self.fo.fill_second_form(date=self.date, index=self.rental_period, color=self.color, comment=self.comment)
        self.fo.fill_second_form_button_next()
        self.fo.button_yes_confirmation_window()
        title = self.fo.get_order_text()
        self.fo.button_check_status_modal_window()
        assert 'Заказ оформлен' in title


    @allure.title('Проверка перехода на страницу формы заказа по клику на нижнюю кнопку')
    def test_button_header_navigation(self, driver):
        self.driver = driver
        bp = BasePage(self.driver)
        bp.click_cookie_accept()
        bp.click_button_order_bottom()
        assert self.driver.find_element(*FirstForm.button_next)


    @allure.title('Проверка перехода на страницу ЯндексДзен')
    def test_logo_yandex_navigation(self, driver):
        self.driver = driver
        bp = BasePage(self.driver)
        bp.click_logo_yandex()
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'


    @allure.title('Проверка перехода на главную страницу Самоката')
    def test_logo_scooter_navigation(self, driver):
        self.driver = driver
        bp = BasePage(self.driver)
        bp.click_logo_scooter()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

