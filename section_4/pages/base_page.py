from selenium.common.exceptions import NoAlertPresentException
import math


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
