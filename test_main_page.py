from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):


    # Гость открывает главную страницу
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()

    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()

    # Ожидаем, что в корзине нет товаров
    basketPage = BasketPage(browser, link)
    basketPage.empty_basket_check()

    # Ожидаем, что есть текст о том что корзина пуста
    basketPage.should_be_text_basket_is_empty()

@pytest.mark.skip
def test_guest_can_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()
    # Ожидаем, что в корзине есть товары
    basketPage = BasketPage(browser, link)
    basketPage.not_empty_basket_check()
    # Ожидаем, что нет текста о том что корзина пуста
    basketPage.not_should_be_text_basket_is_empty()