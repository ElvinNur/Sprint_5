from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Проверь переход по клику на «Личный кабинет»
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")

driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default']").send_keys("elvinnurmamedov13@ya.ru")
driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("qwertyu")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
driver.find_element(By.XPATH, "(//p[@class='AppHeader_header__linkText__3q_va ml-2'])[3]").click()  # клик по кнопке "Личный кабинет"
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']"))) # проверка на наличие текста "В этом разделе вы можете изменить свои персональные данные"
driver.quit()
# fortest