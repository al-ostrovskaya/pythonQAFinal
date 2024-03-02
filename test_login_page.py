from .pages.login_page import LoginPage
import time


def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.can_see_forms()

def test_register_new_user(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.register_new_user(str(time.time()) + "@pythonmail.ru", str(time.time()) + "Password123!!!")
    page.should_be_authorized_user()