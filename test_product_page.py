from .pages.product_page import PageObject
import pytest


#@pytest.mark.parametrize('num', ["0","1","2","3","4","5","6",pytest.param("7", marks=pytest.mark.xfail),"8","9"])
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = PageObject(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.match_book_name()
    page.match_price()
    page.success_message_should_disappear()
