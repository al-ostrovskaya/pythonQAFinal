from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_promo(self):
        assert "promo" in self.browser.current_url, "No Promo"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


    def should_be_message_of_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Element is not desappeared"
        )

    def product_in_basket_match_added(self, browser):
        name = browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_text = name.text
        alertinner = browser.find_element(*ProductPageLocators.ALERTINNER)
        add_result = alertinner.text
        assert name_text == add_result, \
            f"В корзину был добавлен товар, отличный от выбранного {name_text}"


    def price_in_basket_match_added(self, browser):
        price = browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_text = price.text
        cart_price = browser.find_element(*ProductPageLocators.CART_PRICE)
        cart_price_text = cart_price.text

        assert price_text in cart_price_text, \
            f"Сумма корзины {cart_price_text} не совпадает с ценой товара {price_text}"