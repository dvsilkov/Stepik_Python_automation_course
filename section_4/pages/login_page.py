# Теперь реализуем Page Object, который будет связан со страницей логина интернет-магазина.

# нужно сделать импорт базового класса BasePage
from section_4.pages.base_page import BasePage

# Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать:
from selenium.common.exceptions import NoSuchElementException

# импортируйте новый класс с локаторами
from section_4.pages.locators import LoginPageLocators

class LoginPage(BasePage):
    # в этом классе реализуем метод is_element_present, в котором будем перехватывать исключение.
    # В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
    def if_element_presented(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        cur_url = self.browser.current_url
        assert 'login' in cur_url.text, 'The URL is not correct. Correct link is "http://selenium1py.pythonanywhere.com/ru/accounts/login/"'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.if_element_presented(*LoginPageLocators.login_form_locator), 'Login form is missing in the login page'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.if_element_presented(*LoginPageLocators.reg_form_locator), 'Register form is missing in the login page'