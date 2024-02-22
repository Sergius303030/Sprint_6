import pytest
from selenium import webdriver

base_url = 'https://qa-scooter.praktikum-services.ru/'

@pytest.fixture()
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)
    driver.get(base_url)
    yield driver
    driver.quit()