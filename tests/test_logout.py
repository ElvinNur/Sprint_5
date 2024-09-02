from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")

driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default']").send_keys("elvinnurmamedov13@ya.ru")
driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("qwertyu")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
driver.find_element(By.XPATH, "(//p[@class='AppHeader_header__linkText__3q_va ml-2'])[3]").click() # клик по кнопке "Личный кабинет"

logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button")))
logout_button.click() # клик по кнопке "Выход"

WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > h2"))) # проверка на наличие текста "Вход"
driver.quit()
# fortest