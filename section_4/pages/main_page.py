from selenium.webdriver.common.by import By

# Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать:
from  selenium.common.exceptions import NoSuchElementException

# Теперь реализуем Page Object, который будет связан с главной страницей интернет-магазина.

# нужно сделать импорт базового класса BasePage
from section_4.pages.base_page import BasePage

# импортируйте новый класс с локаторами
from section_4.pages.locators import MainPageLocators

# Создаем класс  MainPage. Его нужно сделать наследником класса BasePage. Класс-предок в Python указывается в скобках:
# таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка.
class MainPage(BasePage):
    # в этом классе реализуем метод is_element_present, в котором будем перехватывать исключение.
    # В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
    def if_element_presented(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Создаем метод для нажатия кнопки, нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса:
    def go_to_login_page(self):
        # Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью self

        # без использования файла locators.py
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        #login_link.click()

        # с использование файла locators.py
        login_link = self.browser.find_element(*MainPageLocators.Login_Link)
        login_link.click()

    # нужно реализовать метод, который будет проверять наличие ссылки. Обычно все такие методы-проверки называются
    # похожим образом, мы будем называть их should_be_(название элемента).
    # для получения сообщения используем assert и метод проверки элемента
    def should_be_login_link(self):
        # без использования файла locators.py
        #assert self.if_element_presented(By.CSS_SELECTOR, "#registration_link"), "Login link is not presented"

        # с использование файла locators.py
        assert self.if_element_presented(*MainPageLocators.Login_Link), "Login link is not presented"

