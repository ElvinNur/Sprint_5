from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import FILLINGS_TAB, SAUCES_TAB, BUNS_TAB, FILLINGS_HEADER, SAUCES_HEADER, BUNS_HEADER



def test_section_navigation(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    # Клик "Начинки" и проверка заголовка
    driver.find_element(*FILLINGS_TAB).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(FILLINGS_HEADER))

    # Клик "Соусы" и проверка заголовка
    driver.find_element(*SAUCES_TAB).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(SAUCES_HEADER))

    # Клик "Булки" и проверка заголовка
    driver.find_element(*BUNS_TAB).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BUNS_HEADER))