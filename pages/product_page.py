from .base_page import BasePage
from .locators import ProductPageLocators


class PageObject(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def match_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).text
        assert book_name == book_in_basket, "Названия книг не сопадают"

    def match_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert book_price == basket_price, "Цены не совпадают"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but it must disappear"