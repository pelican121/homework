from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x): return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    
    #time.sleep(2)
    
    target_field = browser.find_element(By.CSS_SELECTOR, "input#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", target_field)
    target_field.send_keys(y)
    
    #time.sleep(2)
    
    target_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", target_checkbox)
    target_checkbox.click()
    
    #time.sleep(2)
    
    target_radio = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", target_radio)
    target_radio.click()
    
    #time.sleep(2)
    
    target_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", target_submit)
    target_submit.click()

finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла