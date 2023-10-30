#https://stepik.org/lesson/228249/step/4?unit=200781

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
    
finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла