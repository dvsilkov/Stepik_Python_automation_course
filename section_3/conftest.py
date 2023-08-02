import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose any language")

# Фикстура для запуска и закрытия экземпляра браузера Chrome или Firefox
# Запуск тестов c параметрами
@pytest.fixture(scope="function")
def browser(request):
    # запрос параметров
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    # выбор языка в браузере для Chrome
    options_chrome = Options()
    options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # выбор языка в браузере для Firefox
    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    browser_obj = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser_obj = webdriver.Chrome(options=options_chrome)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser_obj = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser_obj
    print("\nquit browser..")
    browser_obj.quit()