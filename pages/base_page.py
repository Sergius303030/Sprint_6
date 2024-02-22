import time
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        self.driver.find_element(*MainPage.button_coockie_confirm).click()

    @allure.step('Клик по верхней кнопке "Заказать"')
    def click_button_order_header(self):
        self.wait.until(EC.element_to_be_clickable(MainPage.button_order_header))
        self.driver.find_element(*MainPage.button_order_header).click()

    @allure.step('Скролл до нижней кнопки "Заказать"')
    def scroll_button_order_bottom(self):
        el = self.driver.find_element(*MainPage.sroll_button_body)
        self.driver.execute_script('arguments[0].scrollIntoView();', el)
        self.wait.until(EC.visibility_of_element_located(MainPage.sroll_button_body))
        self.wait.until(EC.element_to_be_clickable(MainPage.button_order_bottom))

    @allure.step('Клик по нижней кнопке "Заказать"')
    def click_button_order_bottom(self):
        self.driver.find_element(*MainPage.button_order_bottom).click()

    @allure.step('Клик по логотипу Самоката')
    def click_logo_scooter(self):
        self.driver.find_element(*MainPage.logo_scooter).click()
        self.wait.until(EC.url_to_be('https://qa-scooter.praktikum-services.ru/'))

    @allure.step('Клик по логотипу Яндекса')
    def click_logo_yandex(self):
        self.wait.until(EC.element_to_be_clickable(MainPage.logo_yandex))
        self.driver.find_element(*MainPage.logo_yandex).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(10)
