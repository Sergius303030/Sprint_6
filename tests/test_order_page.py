import allure
import pytest
from pages.order_page import FormOrder
from locators.order_page_locators import FirstForm
from conftest import *
from parametrize.parametrize import UserData


class TestFormOrder:
    @allure.title('Проверка успешного сценария создания заказа')
    @pytest.mark.parametrize('firstname, surname, address, station, phone, date, rental_period, color, comment', UserData.data_user)
    def test_order_succsess(self, firstname, surname, address, station, phone, date, rental_period, color, comment, driver):
        self.driver = driver
        self.fo = FormOrder(self.driver)
        self.fo.click_cookie_accept()
        self.fo.click_button_order_header()
        self.firstname = firstname
        self.surname = surname
        self.address = address
        self.station = station
        self.phone = phone
        self.date = date
        self.rental_period = rental_period
        self.color = color
        self.comment = comment
        self.fo.fill_full_order(self.firstname, self.surname, self.address,
                           self.station, self.phone, self.date, self.rental_period,
                           self.color, self.comment)
        title = self.fo.get_order_text()
        self.fo.button_check_status_modal_window()
        assert 'Заказ оформлен' in title


    @allure.title('Проверка перехода на страницу формы заказа по клику на нижнюю кнопку')
    def test_button_header_navigation(self, driver):
        self.driver = driver
        fo = FormOrder(self.driver)
        fo.click_cookie_accept()
        fo.click_button_order_bottom()
        assert self.driver.find_element(*FirstForm.button_next)


    @allure.title('Проверка перехода на страницу ЯндексДзен')
    def test_logo_yandex_navigation(self, driver):
        self.driver = driver
        fo = FormOrder(self.driver)
        fo.click_logo_yandex()
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'


    @allure.title('Проверка перехода на главную страницу Самоката')
    def test_logo_scooter_navigation(self, driver):
        self.driver = driver
        fo = FormOrder(self.driver)
        fo.click_logo_scooter()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

