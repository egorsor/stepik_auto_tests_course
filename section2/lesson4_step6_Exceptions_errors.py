#https://stepik.org/lesson/181384/step/6?unit=156009

#Какую ошибку вы увидите в консоли,
#если попытаетесь выполнить команду browser.find_element(By.ID, "button")
#после открытия страницы http://suninjuly.github.io/cats.html?

#NoSuchElementException - если элемент не был найден за отведенное время
#StaleElementReferenceException - если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился 
#ElementNotVisibleException - если элемент был найден в момент поиска, но сам элемент невидим.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome() 

try:
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/cats.html")

    button = browser.find_element(By.ID, "button")
    button.click()
    
finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла