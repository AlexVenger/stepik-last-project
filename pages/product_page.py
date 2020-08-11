from .base_page import BasePage
from .locators import ProductPageLocators


class PageObject(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()
        BasePage.solve_quiz_and_get_code(self)

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "There's no add to cart button"

    def product_name_should_be(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME).text
        assert name == message, f'Should be {name}, not {message}'

    def product_price_should_be(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        assert price == message, f'Should be {price}, not {message}'
