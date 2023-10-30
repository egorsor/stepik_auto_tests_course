#https://stepik.org/lesson/165493/step/6?unit=140087

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #поиск радио-батон
    people_radio = browser.find_element(By.ID, "peopleRule")
    
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    
    #поиск радио-батон2
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots radio: ", robots_checked)
    
    assert robots_checked is not None, "Robots radio is not selected by default"
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла