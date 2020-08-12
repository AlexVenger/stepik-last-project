from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), "Basket is not empty but it has to"

    def is_message_of_empty_basket_appear(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        empty_message = "Your basket is empty. Continue shopping"
        assert message == empty_message, "Empty basket message is not present"

    def should_be_basket_button(self):
        assert self.is_element_present(*BasePageLocators.BASKET_BUTTON), "Basket is not found"

    def should_not_be_basket_button(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_BUTTON), \
            "Basket is here although it shouldn't be here"
