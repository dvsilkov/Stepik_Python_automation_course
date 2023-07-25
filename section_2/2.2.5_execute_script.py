import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# Если посмотреть на эту страницу то увидим, что огромный футер действительно перекрывает нужную
# нам кнопку. Футером (footer) называется нижний блок, который обычно одинаков для всех страниц сайта.
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")

# В метод execute_script мы передали текст js-скрипта и найденный элемент button, к которому нужно будет проскроллить страницу.
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

'''
Также можно проскроллить всю страницу целиком на строго заданное количество пикселей. 
Эта команда проскроллит страницу на 100 пикселей вниз:

browser.execute_script("window.scrollBy(0, 100);")
'''

'''
Для сравнения приведем скрипт на этом языке, который делает то же, что приведенный выше пример для WebDriver:

// javascript
button = document.getElementsByTagName("button")[0];
button.scrollIntoView(true);
Можете попробовать исполнить его в консоли браузера на странице http://suninjuly.github.io/execute_script.html.
'''
time.sleep(5)
browser.quit()
