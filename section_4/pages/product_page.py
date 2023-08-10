# Теперь реализуем Page Object, который будет связан со страницей товара в интернет-магазине

# нужно сделать импорт базового класса BasePage
from section_4.pages.base_page import BasePage

# Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать:
from selenium.common.exceptions import NoSuchElementException

# импортируйте новый класс с локаторами
from section_4.pages.locators import ProductPageLocators

# Создать класс Page Object с методами для страницы товара
class ProductPage(BasePage):
    # Метод добавления товара в корзину
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.add_to_basket_button_locator)
        add_to_basket_button.click()

    # Метод проверки, что добавление товара в корзину прошло успешно
    def should_be_product_added_to_basket(self):
        self.should_be_message_adding()
        self.should_be_matching_product_name()
        self.should_be_message_basket_cost()
        self.should_be_matching_price()

    # Метод проверки, что есть сообщение о добавлении товара в корзину
    def should_be_message_adding(self):
        assert self.if_element_presented(*ProductPageLocators.product_name_added_message_locator), 'The message about added product is missing'

    # Метод проверки, что сообщение о добавлении товара не появилось, в течение указанного времени
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.product_name_added_message_locator), "Success message is presented, but should not be"

    # Метод проверки, что сообщение о добавлении товара исчезло
    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.product_name_added_message_locator), "Success message is not disappeared, but should not be"

    # Метод проверки, что название товара в сообщении совпадает с тем товаром, который вы действительно добавили
    def should_be_matching_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.product_name_locator).text
        product_name_added = self.browser.find_element(*ProductPageLocators.product_name_added_message_locator).text
        assert product_name == product_name_added, 'The product name does not match'

    # Метод проверки, что есть сообщение о стоимости корзины
    def should_be_message_basket_cost(self):
        assert self.if_element_presented(*ProductPageLocators.basket_cost_message_locator), 'The message about basket cost is missing'

    # Метод проверки, что стоимость корзины в сообщении совпадает с ценой товара, который вы  добавили
    def should_be_matching_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.product_price_locator).text
        #print(product_price)
        basket_cost_message = self.browser.find_element(*ProductPageLocators.basket_cost_message_locator).text
        #print(basket_cost_message)
        assert product_price == basket_cost_message, 'The product price is not equal basket cost'