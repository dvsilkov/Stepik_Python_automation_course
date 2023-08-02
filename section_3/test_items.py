import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# Фикстура browser_param добавлена в conftest.py
def test_item(browser):
    browser.get(link)
    time.sleep(10)
    add_button = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket'")
    assert len(add_button.text) > 0, "Кнопка, чтобы добавить товар в корзину отсутствует"