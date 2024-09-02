import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import REGISTER_NAME_INPUT, REGISTER_EMAIL_INPUT, REGISTER_PASSWORD_INPUT, REGISTER_BUTTON, LOGIN_BUTTON_ON_REGISTER_PAGE

def test_registration_with_random_email(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Генерация трех случайных цифр
    random_digits = random.randint(100, 999)

    # Форматирование логина
    login = f"elvinnurmamedov13{random_digits}@ya.ru"

    # Выполняем регистрацию
    driver.find_element(*REGISTER_NAME_INPUT).send_keys("Elvin")  # Имя
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(login)  # Логин
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("qwertyu")  # Пароль
    driver.find_element(*REGISTER_BUTTON).click()

    # Проверка на наличие кнопки "Войти"
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LOGIN_BUTTON_ON_REGISTER_PAGE))