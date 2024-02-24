from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import time
import pytest


@pytest.mark.parametrize('promo', ["0", "1","2","3","4","5","6","7","8","9"])
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

    browser.close()

