from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name_field = browser.find_element(By.CLASS_NAME, "first")
    first_name_field.send_keys("Rogal")
    
    last_name_field = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last name')]")
    last_name_field.send_keys("Dorn")
    
    email_field = browser.find_element(By.CSS_SELECTOR, "input.third")
    email_field.send_keys("rogal@mail.ru")
    
    #phone_field = browser.find_element(By.XPATH, "//label[contains(text(), 'Phone')]/following::input[1]]")
    #phone_field.send_keys("+79805450999")
    
    #address_field = browser.find_element(By.XPATH, "//label[contains(text(), 'Phone')]/../following-sibling::div/input")
    #address_field.send_keys("moiseeva 69")
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()