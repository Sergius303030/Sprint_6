from selenium.webdriver.common.by import By

class MainPage:
    button_coockie_confirm = (By.ID, 'rcc-confirm-button')
    home_page = [By.CLASS_NAME, 'Home_HomePage__ZXKIX']
    questions = (By.CLASS_NAME, 'accordion')
    question_0 = (By.XPATH, './/*[contains(@id, "accordion__heading-0")]')
    question_1 = (By.XPATH, './/*[contains(@id, "accordion__heading-1")]')
    question_2 = (By.XPATH, './/*[contains(@id, "accordion__heading-2")]')
    question_3 = (By.XPATH, './/*[contains(@id, "accordion__heading-3")]')
    question_4 = (By.XPATH, './/*[contains(@id, "accordion__heading-4")]')
    question_5 = (By.XPATH, './/*[contains(@id, "accordion__heading-5")]')
    question_6 = (By.XPATH, './/*[contains(@id, "accordion__heading-6")]')
    question_7 = (By.XPATH, './/*[contains(@id, "accordion__heading-7")]')
    responce_0 = (By.ID, 'accordion__panel-0')
    responce_1 = (By.ID, 'accordion__panel-1')
    responce_2 = (By.ID, 'accordion__panel-2')
    responce_3 = (By.ID, 'accordion__panel-3')
    responce_4 = (By.ID, 'accordion__panel-4')
    responce_5 = (By.ID, 'accordion__panel-5')
    responce_6 = (By.ID, 'accordion__panel-6')
    responce_7 = (By.ID, 'accordion__panel-7')
    button_order_header = (By.XPATH, "(//button[text()='Заказать'])[1]")
    sroll_button_body = (By.CLASS_NAME, 'Home_FinishButton__1_cWm')
    button_order_bottom = (By.XPATH, "(//button[text()='Заказать'])[2]")
    logo_scooter = (By.XPATH, ".//*[@alt='Scooter']")
    logo_yandex = (By.XPATH, ".//*[@alt='Yandex']")
