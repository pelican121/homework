import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x): return str(math.log(abs(12*math.sin(int(x)))))
    
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)
    b = browser.find_element(By.ID, "input_value")
    x = b.text
    y = calc(x)
    
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
finally:
    time.sleep(10)
    browser.quit()
    
