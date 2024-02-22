import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SectionQuestions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    @allure.step('Клик по вопросу')
    def click_question(self, question):
        self.wait.until(EC.visibility_of_element_located(question))
        fe = self.driver.find_element(*question)
        self.driver.execute_script('arguments[0].scrollIntoView();', fe)
        self.wait.until(EC.visibility_of_element_located(question))
        self.wait.until(EC.element_to_be_clickable(question))
        self.driver.find_element(*question).click()

    @allure.step('Получить текст ответа')
    def text_responce(self, responce):
        return self.driver.find_element(*responce).text

