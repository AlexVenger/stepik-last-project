from pages.product_page import PageObject
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PageObject(browser, link)
    page.open()
    page.add_to_cart()
    time.sleep(10)
    page.product_name_should_be()
    page.product_price_should_be()


def test_guest_should_see_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PageObject(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
