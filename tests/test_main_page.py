import allure
import pytest
from pages.main_page import SectionQuestions
from parametrize.parametrize import SectionQuestionsData
from conftest import *


class TestSectionQuestions:
    @allure.title('Проверка раздела «Вопросы о важном»')
    @pytest.mark.parametrize('question, responce, text_responce', SectionQuestionsData.data)
    def test_section_questions_check_text(self, question, responce, text_responce, driver):
        self.driver = driver
        sq = SectionQuestions(self.driver)
        sq.click_cookie_accept()
        sq.click_question(question)
        text = sq.text_responce(responce)
        assert text == text_responce
