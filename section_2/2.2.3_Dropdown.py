'''
Напишите код, который реализует следующий сценарий:
Открыть страницу https://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с
числом. Отправьте полученное число в качестве ответа для этого задания.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elem1 = int(browser.find_element(By.ID, 'num1').text)
    elem2 = int(browser.find_element(By.ID, 'num2').text)
    sum_elem = elem2 + elem1

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(sum_elem))

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла