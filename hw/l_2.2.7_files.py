import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    
    browser.find_element(By.NAME, "firstname").send_keys("Rogal")
    #time.sleep(2)
    browser.find_element(By.NAME, "lastname").send_keys("Dorn")
    #time.sleep(2)
    browser.find_element(By.NAME, "email").send_keys("Rogal@mail.ru")
    #time.sleep(2)
    browser.find_element(By.ID, "file").send_keys(file_path)
    #time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    #time.sleep(2)
    
finally:
    time.sleep(10)
    browser.quit()
