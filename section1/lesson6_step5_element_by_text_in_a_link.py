#https://stepik.org/lesson/138920/step/5?unit=196194

#На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:

#1 открыть страницу: http://suninjuly.github.io/find_link_text
#2 добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой: str(math.ceil(math.pow(math.pi, math.e)*10000))
#3 кликнуть по найденной ссылке
#4 заполнить скриптом форму регистрации
#5 нажать кнопку Sumbit

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    #1
    browser = webdriver.Chrome()
    browser.get(link)
    
    #2
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    
    #3
    link = browser.find_element(By.LINK_TEXT, text)
    link.click()
    
    #4
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    
    #5
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла