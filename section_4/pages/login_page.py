# Теперь реализуем Page Object, который будет связан со страницей логина интернет-магазина.

# нужно сделать импорт базового класса BasePage
from section_4.pages.base_page import BasePage

# импортируйте новый класс с локаторами
from section_4.pages.locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        cur_url = self.browser.current_url
        assert 'login' in cur_url, 'The URL is not correct. Correct link is "http://selenium1py.pythonanywhere.com/ru/accounts/login/"'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.if_element_presented(*LoginPageLocators.login_form_locator), 'Login form is missing in the login page'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.if_element_presented(*LoginPageLocators.reg_form_locator), 'Register form is missing in the login page'