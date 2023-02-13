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


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form>button:nth-child(3)")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6>h1")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner>strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".row>.col-sm-6:nth-child(2)>p:nth-child(2)")
    PRICE_BASKET = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3)>.alertinner>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)")