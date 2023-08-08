# Теперь реализуем Page Object, который будет связан со страницей товара в интернет-магазине

# нужно сделать импорт базового класса BasePage
from section_4.pages.base_page import BasePage

# Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать:
from selenium.common.exceptions import NoSuchElementException

# импортируйте новый класс с локаторами
from section_4.pages.locators import ProductPageLocators

# Создать класс Page Object с методами для страницы товара
class ProductPage(BasePage):
    # в этом классе реализуем метод is_element_present, в котором будем перехватывать исключение.
    # В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
    def if_element_presented(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.add_to_basket_button_locator)
        add_to_basket_button.click()

    def should_be_product_added_to_basket(self):
        self.should_be_message_adding()
        self.should_be_matching_product_name()
        self.should_be_message_basket_cost()
        self.should_be_matching_price()

    def should_be_message_adding(self):
        # Проверка, что есть сообщение о добавлении товара в корзину
        assert self.if_element_presented(*ProductPageLocators.product_name_added_message_locator), 'The message about added product is missing'

    def should_be_matching_product_name(self):
        # реализуйте проверку, что название товара в сообщении совпадает с тем товаром, который вы действительно добавили
        product_name = self.browser.find_element(*ProductPageLocators.product_name_locator).text
        product_name_added = self.browser.find_element(*ProductPageLocators.product_name_added_message_locator).text
        assert product_name == product_name_added, 'The product name does not match'

    def should_be_message_basket_cost(self):
        # Проверка, что есть сообщение о стоимости корзины
        assert self.if_element_presented(*ProductPageLocators.basket_cost_message_locator), 'The message about basket cost is missing'

    def should_be_matching_price(self):
        # реализуйте проверку, что стоимость корзины в сообщении совпадает с ценой товара, который вы  добавили
        product_price = self.browser.find_element(*ProductPageLocators.product_price_locator).text
        #print(product_price)
        basket_cost_message = self.browser.find_element(*ProductPageLocators.basket_cost_message_locator).text
        #print(basket_cost_message)
        assert product_price == basket_cost_message, 'The product price is not equal basket cost'