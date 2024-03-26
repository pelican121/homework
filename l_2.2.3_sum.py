from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

#target_link = "http://suninjuly.github.io/selects1.html"

  
try:
    browser = webdriver.Chrome()
    # browser.get(target_link)
    
    # num1 = browser.find_element(By.ID, "num1")
    # num2 = browser.find_element(By.ID, "num2")
    # x = num1.text
    # y = num2.text
    # sum = str(int(x) + int(y))
    # print(x, y)
    # choice = Select(browser.find_element(By.TAG_NAME, "select"))
    # choice.select_by_value(sum)
    # browser.find_element(By.TAG_NAME, "button").click()
    
    # print(sum)
    
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
     
finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла