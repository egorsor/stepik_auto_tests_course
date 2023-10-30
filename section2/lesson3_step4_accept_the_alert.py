#https://stepik.org/lesson/184253/step/4?unit=158843

#1 Открыть страницу http://suninjuly.github.io/alert_accept.html
#2 Нажать на кнопку
#3 Принять confirm
#4 На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    
    #1
    browser.get(link)
    
    #2
    btn = browser.find_element(By.TAG_NAME, "button")
    btn.click()
    
    #3
    alert = browser.switch_to.alert
    alert.accept()
    
    #4
    #x
    x = int(browser.find_element(By.ID, "input_value").text)
    
    #считаем уравнение
    y = calc(x)
    
    #поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    #нажимаем кнопку
    btn = browser.find_element(By.TAG_NAME, "button")
    btn.click()
    time.sleep(1)
    
    print(browser.switch_to.alert.text.split(': ')[1])
    
finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла