import pytest

# нужно импортировать классы, описывающие страницы методы для которых будем использовать:
from section_4.pages.product_page import ProductPage
import time

@pytest.mark.xfail(reason='Expected')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    #link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()
    #time.sleep(5)

def test_guest_cant_see_success_message(browser):
    #link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    #time.sleep(5)

@pytest.mark.xfail(reason='Expected')
def test_message_disappeared_after_adding_product_to_basket(browser):
    #link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message_disappeared()
    #time.sleep(5)
