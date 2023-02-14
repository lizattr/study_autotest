from .pages.product_page import PageObject
import pytest


@pytest.mark.xfail(reason="Мы искали баг, и мы его нашли")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Мы снова искали баг, и мы снова его нашли")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_should_disappear()
