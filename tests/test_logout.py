import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

def test_login_and_logout(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Вводим данные для входа
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("elvinnurmamedov13@ya.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("qwertyu")
    driver.find_element(*LOGIN_BUTTON).click()

    # Переход в личный кабинет
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    # Ожидание и клик по кнопке "Выход"
    logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGOUT_BUTTON))
    logout_button.click()

    # Проверка на наличие текста "Вход"
    login_header_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LOGIN_PAGE_HEADER))
    login_header_text = login_header_element.text

    # Используем assert для проверки текста заголовка
    assert login_header_text == "Вход", f"Expected header to be 'Вход' but got '{login_header_text}'"