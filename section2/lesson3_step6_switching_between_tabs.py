#https://stepik.org/lesson/184253/step/6?unit=158843

#1 Открыть страницу http://suninjuly.github.io/redirect_accept.html
#2 Нажать на кнопку
#3 Переключиться на новую вкладку
#4 Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

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
    first_window = browser.window_handles[0] #первая вкладка вкладка
    new_window = browser.window_handles[1] #новая вкладка
    
    browser.switch_to.window(new_window)
    time.sleep(0.5)
    
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
    
    alert = browser.switch_to.alert
    alert.accept()
    
    browser.switch_to.window(first_window)
    time.sleep(0.5)
    
finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла