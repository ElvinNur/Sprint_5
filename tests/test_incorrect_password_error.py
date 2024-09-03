import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


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
    error_message_element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PASSWORD_ERROR_MESSAGE))
    error_message_text = error_message_element.text

    # Используем assert для проверки текста ошибки
    assert error_message_text == "Некорректный пароль", f"Expected error message to be 'Некорректный пароль' but got '{error_message_text}'"