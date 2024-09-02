import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import REGISTER_NAME_INPUT, REGISTER_EMAIL_INPUT, REGISTER_PASSWORD_INPUT, REGISTER_BUTTON, PASSWORD_ERROR_MESSAGE


def test_registration_with_invalid_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Генерация трех случайных цифр
    random_digits = random.randint(100, 999)

    # Форматирование логина
    login = f"elvinnurmamedov13{random_digits}@ya.ru"

    # Выполняем регистрацию
    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Elvin")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(login)
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("1")
    driver.find_element(*REGISTER_BUTTON).click()

    # Проверка на наличие текста "Некорректный пароль"
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PASSWORD_ERROR_MESSAGE))