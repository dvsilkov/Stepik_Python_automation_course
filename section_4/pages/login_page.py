# Теперь реализуем Page Object, который будет связан со страницей логина интернет-магазина.

# нужно сделать импорт базового класса BasePage
from section_4.pages.base_page import BasePage

# импортируйте новый класс с локаторами
from section_4.pages.locators import LoginPageLocators

class LoginPage(BasePage):
    # метод, который принимает две строки и регистрирует пользователя
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.input_email_locator)
        input_email.send_keys(email)

        input_password1 = self.browser.find_element(*LoginPageLocators.input_password1_locator)
        input_password1.send_keys(password)

        input_password2 = self.browser.find_element(*LoginPageLocators.input_password2_locator)
        input_password2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.button_register_locator)
        register_button.click()

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