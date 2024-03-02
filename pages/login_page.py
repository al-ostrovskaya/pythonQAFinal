from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()

    def can_see_forms(self):
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not Login Page url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "No registration form"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_SING_UP).send_keys(email)
        pas_input_1 = self.browser.find_element(*LoginPageLocators.PASS_SING_UP_1).send_keys(password)
        pas_input_2 = self.browser.find_element(*LoginPageLocators.PASS_SING_UP_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BTN_SING_UP).click()