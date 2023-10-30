#https://stepik.org/lesson/165493/step/7?unit=140087

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #поиск сундука
    sunduk = browser.find_element(By.TAG_NAME, "img")
    x = sunduk.get_attribute("valuex")
    
    #считаем уравнение
    y = calc(x)
    
    #подставляем ответ в поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    time.sleep(1)
    
    #выбираем чек-бокс
    checkBox1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkBox1.click()
    time.sleep(1)
    
    #выбираем радио-батон
    radio1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio1.click()
    time.sleep(1)
    
    #нажимаем кнопку
    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()
    time.sleep(1)
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла