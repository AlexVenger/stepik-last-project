from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert MainPageLocators.LOGIN_LINK, 'URL is not found'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert LoginPageLocators.LOGIN_FORM, 'Login form is not found'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert LoginPageLocators.REGISTER_FORM, 'Register form is not found'

    def register_new_user(self, email, password):
        email_bar = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_bar.send_keys(email)
        password_bar = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_bar.send_keys(password)
        confirm_password_bar = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_password_bar.send_keys(password)
        register = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        register.click()
