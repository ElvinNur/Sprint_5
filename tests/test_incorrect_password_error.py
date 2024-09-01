import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

# Генерация трех случайных цифр
random_digits = random.randint(100, 999)

# Форматирование логина
login = f"elvinnurmamedov13{random_digits}@ya.ru"

# Выполняем регистрацию
driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]").send_keys("Elvin") # Имя
driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]").send_keys(login) # Логин
driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[3]").send_keys("1") # Пароль
driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[@class='input__error text_type_main-default']"))) # проверка на наличие текста "Некорректный пароль"

driver.quit()