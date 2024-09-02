import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, PERSONAL_ACCOUNT_BUTTON, LOGOUT_BUTTON, LOGIN_PAGE_HEADER

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
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LOGIN_PAGE_HEADER))