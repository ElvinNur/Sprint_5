import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    # Создание экземпляра WebDriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()  # Закрытие браузера после выполнения тестов

@pytest.fixture
def login(driver):
    def _login():
        driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default']").send_keys("elvinnurmamedov13@ya.ru")
        driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("qwertyu")
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    return _login

# fortest