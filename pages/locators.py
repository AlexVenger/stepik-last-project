from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '.register_form')
    EMAIL = (By.CSS_SELECTOR, '#register_form [type="email"]')
    PASSWORD = (By.CSS_SELECTOR, '#register_form [name="registration-password1"]')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#register_form [name="registration-password2"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, '#add_to_basket_form .btn')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    MESSAGE_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    MESSAGE_NAME = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(2) .alertinner')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_CONTENT = (By.CSS_SELECTOR, '.basket-items .row :nth-child(3) [name="form-0-quantity"]')
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner p')
