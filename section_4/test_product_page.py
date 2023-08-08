# нужно импортировать классы, описывающие страницы методы для которых будем использовать:
import pytest

from section_4.pages.product_page import ProductPage
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