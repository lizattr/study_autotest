from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASS = (By.ID, "id_login-password")

    REG_FORM = (By.ID, "register_form")
    AUTH_USERNAME = (By.ID, "id_registration-email")
    AUTH_PASS = (By.ID, "id_registration-password1")
    AUTH_PASS_DOUBLE = (By.ID, "id_registration-password2")
