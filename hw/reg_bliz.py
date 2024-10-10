#import pdb
#import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("https://eu.account.battle.net/login/ru/")

    #поиск поля email по id 
    email_field = browser.find_element(By.ID, 'accountName')
    #email_field.send_keys("test@mail.ru")

    # поиск поля ввода пароля по name
    password_field = browser.find_element(By.NAME, "password")#.send_keys('qwer123')
    #password_field.send_keys("1234")

    # поиск "глаза" в поле пароля по class name
    show_password_button = browser.find_element(By.CLASS_NAME, "show-password")
    #show_password_button.click()

    # поиск всех кнопкок авторизации через другие платформы (google, ps и тд) по css
    login_buttons = browser.find_elements(By.CSS_SELECTOR, "button[role='row']")
    #for login_button in login_buttons:

    # поиск кнопки "авторизоваться" по id
    login_button = browser.find_element(By.ID, 'submit')
    #login_button.click()

    # поиск блока регистрации (первый тэг li из двух) по tag name
    browser.find_element(By.TAG_NAME, "li")

    # поиск ссылки для перехода к регистрации по partial link text
    browser.find_element(By.PARTIAL_LINK_TEXT, "Зарегистрируйте")#.click()

    # поиск ссылки для восстановления доступа (Вы не можете войти?) по xpath
    browser.find_element(By.XPATH, "//li/a[contains(text(), 'не можете')]")#.click()
    
    #time.sleep(5)
    #pdb.set_trace()

finally:
    #time.sleep(4)
    browser.quit()