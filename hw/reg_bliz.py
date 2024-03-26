from selenium import webdriver
import time
import pdb

from selenium.webdriver.common.by import By

try:
    # Создаем экземпляр драйвера для браузера Google Chrome
    driver = webdriver.Chrome()

    # Ждем 5 секунд
    # time.sleep(5)
    pdb.set_trace()

    # Открываем сайт https://eu.account.battle.net/login/ru/
    driver.get("https://eu.account.battle.net/login/ru/")

    # Ждем 5 секунд
    # time.sleep(5)
    pdb.set_trace()

    # Находим поле ввода для почты и вводим значение slargfuck@mail.ru
    email_field = driver.find_element(By.ID, 'accountName')
    email_field.send_keys("slargfuck@mail.ru")

    # Ждем 5 секунд
    # time.sleep(5)
    pdb.set_trace()

    #Клик по кнопке прослушивания капчи
    listen_capcha_button = driver.find_element(By.CSS_SELECTOR, "div#root path")
    listen_capcha_button.click()

    # Находим поле ввода для пароля и вводим значение 1234
    password_field = driver.find_element(By.XPATH, "//div/input[@id='password']")
    password_field.send_keys("1234")

    # Ждем 5 секунд
    # time.sleep(5)
    pdb.set_trace()

    # Нажимаем на кнопку "Просмотр пароля"
    show_password_button = driver.find_element(By.CLASS_NAME, "show-password")
    show_password_button.click()

    # Ждем 5 секунд
    # time.sleep(5)
    pdb.set_trace()

    # Нажимаем на кнопку "Авторизоваться"
    login_button = driver.find_element(By.ID, 'submit')
    login_button.click()

    # Ждем 5 секунд
    # time.sleep(5)
    pdb.set_trace()
finally:
    # Закрываем браузер
    driver.quit()