from selenium.webdriver.common.by import By

class FirstForm:
    name = (By.XPATH, "//input[@placeholder='* Имя']")
    surname = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    station = (By.XPATH, "//input[@placeholder='* Станция метро']")
    click_station = (By.CLASS_NAME, "select-search__select")
    phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, "//button[text()='Далее']")


class SecondForm:
    date = [By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"]
    date_selected = [By.CLASS_NAME, 'react-datepicker__day--selected']
    dropdown = (By.XPATH, ".//*[@class='Dropdown-arrow']")
    dropdown_option = (By.XPATH, ".//*[@class='Dropdown-menu']/div")
    comment = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")
    button_next = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")


class ModalWindow:
    button_confirm = (By.XPATH, "//button[text()='Да']")
    button_check_status = (By.XPATH, "//button[text()='Посмотреть статус']")
    title = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")



