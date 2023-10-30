#https://stepik.org/lesson/228249/step/8?unit=200781

#1 Открыть страницу http://suninjuly.github.io/file_input.html
#2 Заполнить текстовые поля: имя, фамилия, email
#3 Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#4 Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    #1
    browser = webdriver.Chrome()
    browser.get(link)

    #2
    first = browser.find_element(By.NAME, "firstname")
    first.send_keys("name")
    
    second = browser.find_element(By.NAME, "lastname")
    second.send_keys("second name")
    
    mail = browser.find_element(By.NAME, "email")
    mail.send_keys("mail@mail.ru")
    
    #3
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson2_step8_file.txt')
    
    fileLoader = browser.find_element(By.ID, "file")
    fileLoader.send_keys(file_path)
    
    #4
    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()
    
finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла