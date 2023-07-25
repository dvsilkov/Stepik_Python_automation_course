'''
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером,
который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:
Открыть страницу https://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
'''
import math

def calc(value):
  return str(math.log(abs(12*math.sin(int(value)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 200);")

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла