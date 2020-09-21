from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"
link_to_login = 'http://selenium1py.pythonanywhere.com/accounts/login/'

@pytest.mark.login_guest
class TestLoginFormMainPage():
    def test_guest_should_see_login_link(self, browser):
        # Тестирование наличия ссылки на страницу авторизации.
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
  
    def test_guest_can_go_to_login_page(self, browser):
        # Тестирование перехода на страницу аворизации.
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

# Тестирование страницы регистрации/авторизации.
#-----------------------------------------------------

def test_should_be_login_url(browser):
    # Проверка того, что открытая страница это страница авторизации.
    page = LoginPage(browser, link_to_login)
    page.open()
    page.should_be_login_url()

def test_should_be_login_form(browser):
    # Проверка наличия формы авторизации.
    page = LoginPage(browser, link_to_login)
    page.open()
    page.should_be_login_form()

def test_should_be_register_form(browser):
    # Проверка наличия формы регистрации.
    page = LoginPage(browser, link_to_login)
    page.open()
    page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Проверка того, что при переходе в корзину с главной страницы 
    # корзина пуста и есть соответствующее сообщение.
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_items()
    page.should_be_text_about_empty_basket()
