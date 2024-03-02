from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_SING_UP = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_SING_UP_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_SING_UP_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_SING_UP = (By.CSS_SELECTOR, "[value='Register']")

class ProductPageLocators():
    PROMO = "newYear"
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6 h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6 .price_color")
    ALERTINNER = (By.CSS_SELECTOR, "div .alertinner strong")
    CART_PRICE = (By.CSS_SELECTOR, ".basket-mini")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ITEMS_FORM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET = (By.CSS_SELECTOR, 'div#content_inner > p')


