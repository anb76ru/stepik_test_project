from selenium.webdriver.common.by import By

# создадим классы для разных страниц
# зададим для классов набор локаторов
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

    REGISTER_EMAIL = (By.NAME,'registration-email')
    REGISTER_PASSWORD = (By.NAME, 'registration-password1')
    REGISTER_PASSWORD_CONFIRM = (By.NAME, 'registration-password2')

    REGISTER_BUTTON = (By.NAME, 'registration_submit')
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages > div > div')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')

    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6 > h1')
    PRODUCT_NAME_ADDED = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')

    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6 .price_color')
    PRODUCT_PRICE_ADDED = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.btn-group >a')
    TEXT_ABOUT_EMPTY_BASKET = (By.ID, 'content_inner')
