from selenium.webdriver.common.by import By

# Внутри создайте новые классы. Каждый класс будет соответствовать каждому классу PageObject:
class BasePageLocators():
    login_link_locator = (By.CSS_SELECTOR, '#login_link')
    login_link_invalid_locator = (By.CSS_SELECTOR, '#login_link_inc')
    view_basket_button_locator = (By.CSS_SELECTOR, 'a[href="/en-gb/basket/"]')
    user_icon_locator = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    # для каждого селектора создаем кортеж, теперь каждый селектор — это пара: как искать и что искать.
    login_link_locator = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    # для каждого селектора создаем кортеж, теперь каждый селектор — это пара: как искать и что искать.
    reg_form_locator = (By.CSS_SELECTOR, '#register_form')
    login_form_locator = (By.CSS_SELECTOR, '#login_form')
    input_email_locator= (By.CSS_SELECTOR, '#id_registration-email')
    input_password1_locator = (By.CSS_SELECTOR, '#id_registration-password1')
    input_password2_locator = (By.CSS_SELECTOR, '#id_registration-password2')
    button_register_locator = (By.NAME, 'registration_submit')

class ProductPageLocators():
    # для каждого селектора создаем кортеж, теперь каждый селектор — это пара: как искать и что искать.
    add_to_basket_button_locator = (By.CSS_SELECTOR, 'button[class="btn btn-lg btn-primary btn-add-to-basket"]')

    product_name_locator = (By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"] > h1')
    product_name_added_message_locator = (By.CSS_SELECTOR, 'div[class="alertinner "] > strong')

    basket_cost_message_locator = (By.CSS_SELECTOR,'div[class="alertinner "] > p > strong')
    product_price_locator = (By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"] > p[class="price_color"]')

class BasketPageLocators():
    # для каждого селектора создаем кортеж, теперь каждый селектор — это пара: как искать и что искать.
    basket_empty_message_locator = (By.CSS_SELECTOR, '#content_inner')
    basket_not_empty_form_locator = (By.CSS_SELECTOR, 'basket_formset')
