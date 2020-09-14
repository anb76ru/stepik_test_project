from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

    '''login_username = (By.NAME,  'login-username')
    login_password = (By.NAME, 'login-password')
    login_submit = (By.NAME, 'login_submit')

    reg_email = (By.NAME, 'registration-email')
    reg_password = (By.NAME, 'registration-password1')
    reg_password_repaet = (By.NAME, 'registration-password2')
    reg_submit = (By.NAME, 'registration_submit')'''