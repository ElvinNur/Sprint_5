from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, PERSONAL_ACCOUNT_BUTTON, PERSONAL_ACCOUNT_PAGE_HEADER

def test_personal_account_access(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Вводим данные для входа
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("elvinnurmamedov13@ya.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("qwertyu")
    driver.find_element(*LOGIN_BUTTON).click()

    # Переход в личный кабинет
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    # Проверка на наличие текста "В этом разделе вы можете изменить свои персональные данные"
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PERSONAL_ACCOUNT_PAGE_HEADER))