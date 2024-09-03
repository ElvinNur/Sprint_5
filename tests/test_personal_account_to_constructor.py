from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

def test_constructor_and_logo_navigation(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Вводим данные для входа
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("elvinnurmamedov13@ya.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("qwertyu")
    driver.find_element(*LOGIN_BUTTON).click()

    # Переход в личный кабинет
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    # Переход в Конструктор
    driver.find_element(*CONSTRUCTOR_BUTTON).click()
    header_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BURGER_HEADER))
    header_text = header_element.text

    # Используем assert для проверки текста заголовка "Соберите бургер"
    assert header_text == "Соберите бургер", f"Expected header to be 'Соберите бургер' but got '{header_text}'"

    # Переход обратно в личный кабинет и клик на логотип
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*LOGO_BUTTON).click()
    header_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BURGER_HEADER))
    header_text = header_element.text

    # Используем assert для проверки текста заголовка "Соберите бургер"
    assert header_text == "Соберите бургер", f"Expected header to be 'Соберите бургер' but got '{header_text}'"