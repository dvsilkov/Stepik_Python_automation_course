# Теперь реализуем Page Object, который будет связан со страницей корзины.

# нужно сделать импорт базового класса BasePage
from section_4.pages.base_page import BasePage

# импортируйте новый класс с локаторами
from section_4.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    # метод, проверяющий наличие товара, должен выбрасывать ошибку о пустой корзине
    def should_be_not_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.basket_not_empty_form_locator), 'Basket form is not presented, basket is empty'
    # метод, проверяющий сообщение о пустой корзине, должен выдавать ошибку о наличии товара
    def should_be_empty_basket_message(self):
        assert self.if_element_presented(*BasketPageLocators.basket_empty_message_locator), 'Message is missing, basket is not empty'