# нужно импортировать классы, описывающие страницы методы для которых будем использовать:
import pytest

from section_4.pages.product_page import ProductPage
from section_4.pages.login_page import LoginPage
from section_4.pages.basket_page import BasketPage

import time

@pytest.mark.parametrize('promo', ['?promo=offer0',
                                  '?promo=offer1',
                                  '?promo=offer2',
                                  '?promo=offer3',
                                  '?promo=offer4',
                                  '?promo=offer5',
                                  '?promo=offer6',
                                  pytest.param('?promo=offer7', marks=pytest.mark.xfail(reason='The product name does not match')),
                                  '?promo=offer8',
                                  '?promo=offer9'])
def test_guest_can_add_product_to_basket(browser, promo):
    #link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_basket()
    #time.sleep(5)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и текущий url адрес
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    # Гость открывает страницу товара
    page.open()
    # Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и текущий url адрес
    basket_page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров
    basket_page.should_be_not_goods_in_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket_message()
