#https://stepik.org/lesson/181384/step/8?unit=156009

#1 Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#2 Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#3 Нажать на кнопку "Book"
#4 Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome() 

try:
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    
    #1
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
   
    button.click()
    
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID, "input_value")) #скрол
    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)
    
    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(y)
       
    time.sleep(0.5)
    button = browser.find_element(By.ID, "solve")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла

price