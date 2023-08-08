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

class ProductPageLocators():
    # для каждого селектора создаем кортеж, теперь каждый селектор — это пара: как искать и что искать.
    add_to_basket_button_locator = (By.CSS_SELECTOR, 'button[class="btn btn-lg btn-primary btn-add-to-basket"]')

    product_name_locator = (By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"] > h1')
    product_name_added_message_locator = (By.CSS_SELECTOR, 'div[class="alertinner "] > strong')

    basket_cost_message_locator = (By.CSS_SELECTOR,'div[class="alertinner "] > p > strong')
    product_price_locator = (By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"] > p[class="price_color"]')
