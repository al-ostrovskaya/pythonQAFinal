from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_promo(self):
        assert "promo" in self.browser.current_url, "No Promo"