'''
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element
из библиотеки expected_conditions.
'''
import time
import math

def calc(value):
  return str(math.log(abs(12*math.sin(int(value)))))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
button = browser.find_element(By.ID, 'book')
button.click()

x_elem = browser.find_element(By.ID, "input_value")
x = x_elem.text
y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

button2 = browser.find_element(By.ID, 'solve')
button2.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()