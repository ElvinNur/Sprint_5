from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Проверь, что работают переходы к разделам:
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")


driver.find_element(By.XPATH, "//span[text()='Начинки']").click() # Клик "Начинки"
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Начинки']"))) # проверка на наличие текста "Начинки"

driver.find_element(By.XPATH, "//span[text()='Соусы']").click() # Клик "Соусы"
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Соусы']"))) # проверка на наличие текста "Соусы"

driver.find_element(By.XPATH, "//span[text()='Булки']").click() # Клик "Булки"
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Булки']"))) # проверка на наличие текста "Булки"
driver.quit()