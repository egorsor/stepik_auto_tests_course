#https://stepik.org/lesson/228249/step/6?unit=200781

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #x
    x = int(browser.find_element(By.ID, "input_value").text)
    print(x)
    
    #считаем уравнение
    y = calc(x)
    print(y)
    
    #поле
    input1 = browser.find_element(By.ID, "answer")
    
    #скролл
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    
    #ввод
    input1.send_keys(y)
    time.sleep(1)
    
    #выбираем чек-бокс
    checkBox1 = browser.find_element(By.ID, "robotCheckbox")
    checkBox1.click()
    
    #выбираем радио-батон
    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()
    
    #нажимаем кнопку
    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()
    time.sleep(1)
    
finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла