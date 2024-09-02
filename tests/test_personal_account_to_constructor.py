from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, PERSONAL_ACCOUNT_BUTTON, CONSTRUCTOR_BUTTON, BURGER_HEADER, LOGO_BUTTON

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
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BURGER_HEADER))

    # Переход обратно в личный кабинет и клик на логотип
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*LOGO_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BURGER_HEADER))