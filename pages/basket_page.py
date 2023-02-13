from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):
    def basket_is_empty(self):
        try:
            self.browser.find_element(*BasketPageLocators.BASKET_ITEMS)
        except NoSuchElementException:
            return False
        return "Корзина не пустая"

    def basket_is_empty_notification(self):
        try:
            self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_NOTIFICATION)
        except NoSuchElementException:
            return False
        return "Уведомления нет"
