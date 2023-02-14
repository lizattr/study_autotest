from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cur_url = self.browser.current_url
        assert "login" in cur_url, "Слов о логине в URL нет"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Формы для входа нет на странице"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Формы для регистрации нет на странице"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.AUTH_USERNAME).send_keys(email)
        self.browser.find_element(*LoginPageLocators.AUTH_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.AUTH_PASS_DOUBLE).send_keys(password)
        self.browser.find_element(*LoginPageLocators.AUTH_BUTTON).click()
