# Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать:
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

# импортируйте необходимые классы с локаторами
from section_4.pages.locators import BasePageLocators


# Для начала сделаем базовую страницу, от которой будут унаследованы все остальные классы. В ней мы опишем вспомогательные методы для работы с драйвером.
class BasePage():
    # Теперь в наш класс нужно добавить методы. Первым делом добавим конструктор — метод, который вызывается,
    # когда мы создаем объект. Конструктор объявляется ключевым словом __init__. В него в качестве параметров мы
    # передаем экземпляр драйвера и url адрес. Внутри конструктора сохраняем эти данные как аттрибуты нашего класса.
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # добавим команду для неявного ожидания со значением по умолчанию в 10:
        self.browser.implicitly_wait(timeout)
    # Теперь добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get().
    def open(self):
        self.browser.get(self.url)

    # в этом классе реализуем метод is_element_present, в котором будем перехватывать исключение.
    # В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
    def if_element_presented(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени:
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # Если проверяем, что какой-то элемент исчезает, то нужно явное ожидание вместе с функцией until_not, в зависимости от того, какой результат мы ожидаем:
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # Метод для получения проверочного кода
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # Создаем метод для нажатия кнопки, нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса:
    def go_to_login_page(self):
        # Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью self

        # без использования файла locators.py
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        #login_link.click()

        # с использование файла locators.py
        login_link = self.browser.find_element(*BasePageLocators.login_link_locator)
        login_link.click()

    # нужно реализовать метод, который будет проверять наличие ссылки. Обычно все такие методы-проверки называются
    # похожим образом, мы будем называть их should_be_(название элемента).
    # для получения сообщения используем assert и метод проверки элемента
    def should_be_login_link(self):
        # без использования файла locators.py
        #assert self.if_element_presented(By.CSS_SELECTOR, "#registration_link"), "Login link is not presented"

        # с использование файла locators.py
        assert self.if_element_presented(*BasePageLocators.login_link_locator), "Login link is not presented"

    # Создаем метод для нажатия кнопки добавления в корзину, нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса:
    def go_to_basket_page(self):
        # Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью self

        # с использование файла locators.py
        view_basket_button = self.browser.find_element(*BasePageLocators.view_basket_button_locator)
        view_basket_button.click()