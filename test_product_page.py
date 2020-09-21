from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage

import pytest
import time

product_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear2019'

# run test: pytest -v -s --tb=line --language=en test_product_page.py

def test_guest_should_see_login_link_on_product_page(browser):
    # Тестирование наличия ссылки авторизации/регистрации на странице товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # Тестирование перехода на страницу авторизации со страницы товара.
    # Тестирование на то, что открывшаяся страница является странице авторизации.
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_should_be_product_page_promo(browser):
    # Проверка открывшейся страницы
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_product_page()

def test_should_be_add_to_cart_button(browser):
    # Тестирование наличия ссылки добавления товара в корзину.
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_add_to_cart_link()

@pytest.mark.need_review
def test_guest_add_to_basket_product(browser):
    # Добавление товара в корзину.
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.shoul_be_add_to_basket_message()
    product_page.compare_product_name()
    product_page.compare_product_price()

product_links = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
@pytest.mark.parametrize('link', [f"{product_links}0",
                                  f"{product_links}1",
                                  f"{product_links}2",
                                  f"{product_links}3",
                                  f"{product_links}4",
                                  f"{product_links}5",
                                  f"{product_links}6",
                                  f"{product_links}7", pytest.param('bugget_link', marks=pytest.mark.xfail),
                                  f"{product_links}8",
                                  f"{product_links}9"])

def test_guest_can_add_product_to_basket(browser, link):
    # Добавление товара в корзину с параметризацией. 
    # Поиск багнутой ссылки.
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.shoul_be_add_to_basket_message()
    product_page.compare_product_name()
    product_page.compare_product_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара. 
    # Добавляем товар в корзину.
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present.
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара. 
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present.
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара.
    # Добавляем товар в корзину.
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared.
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_wait_until_element_is_not_present()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Тестирования отсутствия товара в корзине при переходе в нее со страницы товара
    product_page = BasketPage(browser, product_link)
    product_page.open()
    product_page.go_to_basket_page()
    product_page.should_not_be_items()
    product_page.should_be_text_about_empty_basket()

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Общая функция для двух тестов в классе
        email = str(time.time()) + "@fakemail.org"
        password = 'UbxDU52ksjaMZLi'
        product_page = LoginPage(browser, product_link)
        product_page.open()
        product_page.go_to_login_page()
        product_page.register_new_user(email, password)
        product_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Для залогиненного пользователя.
        # Открываем страницу товара. 
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present.
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # Для залогиненного пользователя.
        # Открываем страницу товара. 
        # Добавляем товар в корзину.
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.shoul_be_add_to_basket_message()
        product_page.compare_product_name()
        product_page.compare_product_price()