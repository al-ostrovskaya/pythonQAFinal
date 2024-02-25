from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
import time
import pytest


# @pytest.mark.parametrize('promo', ["0", "1","2","3","4","5","6","7","8","9"])
@pytest.mark.parametrize('promo', ["0"])
def test_guest_can_add_product_to_basket(browser, promo):

    #открытие страницы
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = MainPage(browser, link)
    page.open()

    # проверка на наличие промокода
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_promo()

    # считывание цены и названия товара в переменные
    price = browser.find_element(By.CSS_SELECTOR, ".col-sm-6 .price_color")
    price_text = price.text
    name = browser.find_element(By.CSS_SELECTOR, ".col-sm-6 h1")
    name_text = name.text

    # добавление товара в корзину.
    browser.find_element(By.CSS_SELECTOR, "[value='Добавить в корзину']").click()
    page.solve_quiz_and_get_code()
    time.sleep(5)

    # запись в переменные текста товара из сообщения о добавлении товара и суммы корзины
    alertinner = browser.find_element(By.CSS_SELECTOR, "div .alertinner strong")
    add_result = alertinner.text
    cart_price = browser.find_element(By.CSS_SELECTOR, ".basket-mini")
    cart_price_text = cart_price.text

    #проверки на соответствие товара и цены с итоговой суммой корзины
    assert name_text == add_result, \
        f"В корзину был добавлен товар, отличный от выбранного {name_text}"

    assert price_text in cart_price_text, \
        f"Сумма корзины {cart_price_text} не совпадает с ценой товара {price_text}"

    product_page.should_be_success_message()
    browser.close()
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    # Открываем страницу товара
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, link)
    page.open()
    # Добавляем товар в корзину
    browser.find_element(By.CSS_SELECTOR, "[value='Добавить в корзину']").click()
    page.solve_quiz_and_get_code()
    time.sleep(5)

    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()
    browser.close()



def test_guest_cant_see_success_message(browser):


    # Открываем страницу товара
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, link)
    page.open()

    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()
    browser.close()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):


    # Открываем страницу товара
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, link)
    page.open()
    # Добавляем товар в корзину
    browser.find_element(By.CSS_SELECTOR, "[value='Добавить в корзину']").click()
    page.solve_quiz_and_get_code()
    time.sleep(5)

    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_message_of_is_disappeared()
    browser.close()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(20)

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):


    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке

    page.go_to_basket_page()
    # Ожидаем, что в корзине нет товаров
    basketPage = BasketPage(browser, link)
    basketPage.empty_basket_check()

    # Ожидаем, что есть текст о том что корзина пуста
    basket_info = browser.find_element(By.CSS_SELECTOR, "#content_inner")
    basket_info_text = basket_info.text
    check_text = "Ваша корзина пуста"
    assert  check_text in basket_info_text, \
        f"Корзина не пуста"


@pytest.mark.skip
def test_guest_can_see_product_in_basket_opened_from_product_page(browser):

    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    # Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()

    # Ожидаем, что в корзине есть товары
    basketPage = BasketPage(browser, link)
    basketPage.not_empty_basket_check()

    # Ожидаем, что нет текста о том что корзина пуста
    basketPage.not_empty_basket_text_check()