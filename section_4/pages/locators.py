from selenium.webdriver.common.by import By

# Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу PageObject:
class MainPageLocators():
    # для каждого селектора создаем кортеж, теперь каждый селектор — это пара: как искать и что искать.
    #login_link = (By.CSS_SELECTOR, '#registration_link')
    Login_Link = (By.CSS_SELECTOR, '#login_link')