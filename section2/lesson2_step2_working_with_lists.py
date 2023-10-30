#https://stepik.org/lesson/228249/step/2?unit=200781

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #инициализируем список
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    
    #выбираем по значению value
    select.select_by_value("1")
    time.sleep(2)
    
    #выбираем по видимому тексту
    select.select_by_visible_text("88")
    time.sleep(2)
    
    #выбираем по индексу (порядковому номеру)
    select.select_by_index(4)
    time.sleep(2)
    
finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла