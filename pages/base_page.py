import math

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BasePageLocators
from pages.locators import BasketPageLocators


# Базовая страница, от которой будут унаследованы все остальные классы. 
# В ней мы опишем вспомогательные методы для работы с драйвером
class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        # Метод, который открывает страницу в браузере.
        self.browser.get(self.url)
    
    def go_to_login_page(self):
        # Метод для перехода на страницу авторизации.
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
    
    def should_be_login_link(self):
        # Метод для проверки того, что открытая страния является страницей для регистрации/авторизации.
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        # Метод проверяющий что пользователь авторизован.
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                    " probably unauthorised user"
    
    def is_element_present(self, how, what):
        # Метод для перехвата исключений.  Проверяет наличие элемента на мтранице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def go_to_basket_page(self):
        # Метод для перехода в корзину.
        basket_page = self.browser.find_element(*BasketPageLocators.BASKET_ITEMS)
        basket_page.click()

    def is_not_element_present(self, how, what, timeout=4):
        # Метод проверяющий отсутствие элемента на странице.
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        # Проверка исчезновения элемента. Будет ждать до тех пор, пока элемент не исчезнет.
        # По умолчанию 4 сек.
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        # Ввод капчи
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(answer)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")