from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"
link_to_login = 'http://selenium1py.pythonanywhere.com/accounts/login/'
def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

# тестирование наличия ссылки на страницу авторизации
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# тестирование перехода на страницу аворизации
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# тестирование страницы регистрации/авторизации
def test_should_be_login_url(browser):
    page = LoginPage(browser, link_to_login)
    page.open()
    page.should_be_login_url()

def test_should_be_login_form(browser):
    page = LoginPage(browser, link_to_login)
    page.open()
    page.should_be_login_form()

def test_should_be_register_form(browser):
    page = LoginPage(browser, link_to_login)
    page.open()
    page.should_be_register_form()