# нужно импортировать класс, описывающий главную страницу:
from section_4.pages.main_page import MainPage
from section_4.pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #link = ' http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    page = MainPage(browser, link)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    page.go_to_login_page()             # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и текущий url адрес
    login_page.should_be_login_page()

# добавляем новый тест
def test_guest_should_see_logon_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #link = ' http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    page = MainPage(browser, link)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    page.should_be_login_link()         # выполняем метод страницы — проверяем наличие ссылки
# Убедитесь, что тест работает, с помощью следующей команды: pytest -v --tb=line --language=en test_main_page.py.
# Здесь и далее мы будем использовать эту команду для запуска. В этой команде мы использовали опцию PyTest --tb=line,
# которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста.
# Так вам будет проще разобраться в том, как выглядят сообщения об ошибках.