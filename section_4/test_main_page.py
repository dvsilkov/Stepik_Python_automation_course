from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)

# Убедитесь, что тест работает, с помощью следующей команды: pytest -v --tb=line --language=en test_main_page.py.
# Здесь и далее мы будем использовать эту команду для запуска. В этой команде мы использовали опцию PyTest --tb=line,
# которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста.
# Так вам будет проще разобраться в том, как выглядят сообщения об ошибках.