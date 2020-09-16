from pages.product_page import ProductPage

from pages.product_page import ProductPage
from pages.main_page import MainPage


product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019' #'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

# run test: pytest -v -s --tb=line --language=en test_product_page.py

# проверка открывшейся страницы
def test_should_be_product_page_promo(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_product_page()

# тестирование наличия ссылки добавления товара в корзину

def test_should_be_add_to_cart_button(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_add_to_cart_link()

# добавление товара в корзину
def test_add_to_cart_product(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.shoul_be_add_to_basket_message()
    product_page.compare_product_name()
    product_page.compare_product_price()
    