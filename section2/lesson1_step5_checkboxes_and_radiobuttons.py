#https://stepik.org/lesson/165493/step/5?unit=140087

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #получаем значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    
    #считаем уравнение
    y = calc(x)
    
    #подставляем ответ в поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    
    #выбираем чек-бокс
    checkBox1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkBox1.click()
    
    #выбираем радио-батон
    radio1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio1.click()
    
    #нажимаем кнопку
    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()
    
finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла