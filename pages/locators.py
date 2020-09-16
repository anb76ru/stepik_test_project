from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages > div > div')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')

    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6 > h1')
    PRODUCT_NAME_ADDED = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')

    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6 .price_color')
    PRODUCT_PRICE_ADDED = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')

    '''login_username = (By.NAME,  'login-username')
    login_password = (By.NAME, 'login-password')
    login_submit = (By.NAME, 'login_submit')

    reg_email = (By.NAME, 'registration-email')
    reg_password = (By.NAME, 'registration-password1')
    reg_password_repaet = (By.NAME, 'registration-password2')
    reg_submit = (By.NAME, 'registration_submit')'''