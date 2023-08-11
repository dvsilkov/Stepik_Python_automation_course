import pytest

# нужно импортировать классы, описывающие страницы методы для которых будем использовать:
from section_4.pages.main_page import MainPage
from section_4.pages.login_page import LoginPage
from section_4.pages.basket_page import BasketPage

@pytest.mark.login_guest
# Создадим класс где объединим в группу два теста в файле test_main_page.py и пометим его меткой login_guest:
# Метка login_guest прописана в pytest.ini
# запустить тесты в этом файле с меткой (нужно добавить "-m login_guest"). Вы увидите, что запустились оба теста, хотя метка всего одна.
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        #link = ' http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
        page = MainPage(browser, link)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                         # открываем страницу
        page.go_to_login_page()             # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и текущий url адрес
        login_page.should_be_login_page()

    # добавляем новый тест
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        #link = ' http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
        page = MainPage(browser, link)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                         # открываем страницу
        page.should_be_login_link()         # выполняем метод страницы — проверяем наличие ссылки
    # Убедитесь, что тест работает, с помощью следующей команды: pytest -v --tb=line --language=en test_main_page.py.
    # Здесь и далее мы будем использовать эту команду для запуска. В этой команде мы использовали опцию PyTest --tb=line,
    # которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста.
    # Так вам будет проще разобраться в том, как выглядят сообщения об ошибках.

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    # Гость открывает главную страницу
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и текущий url адрес
    basket_page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров
    basket_page.should_be_not_goods_in_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket_message()