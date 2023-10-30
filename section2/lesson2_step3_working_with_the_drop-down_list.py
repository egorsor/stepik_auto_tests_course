#https://stepik.org/lesson/228249/step/2?unit=200781

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #ищем число 1
    num1 = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)

    #ищем число 2
    num2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    
    #сумма
    summ = num1 + num2
 
    #инициализируем список
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    
    #выбираем по тексту
    select.select_by_visible_text(str(summ))
    time.sleep(1)
    
    #ищем и кликаем Submit
    btn = browser.find_element(By.TAG_NAME, "button")
    btn.click()
    
finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла