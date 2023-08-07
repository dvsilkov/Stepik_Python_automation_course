from selenium.webdriver.common.by import By

# Внутри создайте новые классы. Каждый класс будет соответствовать каждому классу PageObject:
class MainPageLocators():
    # для каждого селектора создаем кортеж, теперь каждый селектор — это пара: как искать и что искать.
    #login_link = (By.CSS_SELECTOR, '#registration_link')
    login_link_locator = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    # для каждого селектора создаем кортеж, теперь каждый селектор — это пара: как искать и что искать.
    reg_form_locator = (By.CSS_SELECTOR, '#register_form')
    login_form_locator = (By.CSS_SELECTOR, '#login_form')
