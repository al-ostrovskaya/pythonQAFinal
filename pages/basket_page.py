from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):

    def empty_basket_check(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_FORM), \
            "Success message is not presented, but should not be"

    def not_empty_basket_check(self):
        assert self.is_element_present(*BasketPageLocators.ITEMS_FORM), \
            "Success message is not presented, but should not be"

    def empty_basket_text_check(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_INFO), \
            "Success message is not presented, but should not be"

    def not_empty_basket_text_check(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_INFO), \
            "Success message is not presented, but should not be"

