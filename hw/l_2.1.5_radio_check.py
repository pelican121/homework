from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

target_link = "http://suninjuly.github.io/get_attribute.html"

def calc(x): return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get(target_link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "img[valuex]")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    time.sleep(2)
    target_field = browser.find_element(By.CSS_SELECTOR, "input#answer")
    target_field.send_keys(y)
    #time.sleep(2)
    target_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    target_checkbox.click()
    time.sleep(2)
    target_radio = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    target_radio.click()
    time.sleep(2)
    target_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    target_submit.click()
    time.sleep(2)
    
    # people_radio = browser.find_element(By.ID, "peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    # assert people_checked == "true", "People radio is not selected by default"
    
    # robots_radio = browser.find_element(By.ID, "robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # assert robots_checked is None
    # print("value of robots radio: ", robots_checked)
     
finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла