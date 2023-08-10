# Теперь реализуем Page Object, который будет связан с главной страницей интернет-магазина.

# нужно сделать импорт базового класса BasePage
from section_4.pages.base_page import BasePage

# Создаем класс  MainPage. Его нужно сделать наследником класса BasePage. Класс-предок в Python указывается в скобках:
# таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка.
class MainPage(BasePage):
    # Все методы переносим в base_page.py, заменяя класс с локаторами на BasePageLocators
    # В классе MainPage у нас не осталось никаких методов, поэтому добавим туда заглушку:
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

