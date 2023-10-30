#https://stepik.org/lesson/228249/step/5?unit=200781

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    time.sleep(3)
    
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    time.sleep(5)
    browser.quit()
    