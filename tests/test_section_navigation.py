from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

def test_section_navigation(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    # Клик "Начинки" и проверка заголовка
    driver.find_element(*FILLINGS_TAB).click()
    fillings_header_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(FILLINGS_HEADER))
    fillings_header_text = fillings_header_element.text
    assert fillings_header_text == "Начинки", f"Expected header to be 'Начинки' but got '{fillings_header_text}'"

    # Клик "Соусы" и проверка заголовка
    driver.find_element(*SAUCES_TAB).click()
    sauces_header_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(SAUCES_HEADER))
    sauces_header_text = sauces_header_element.text
    assert sauces_header_text == "Соусы", f"Expected header to be 'Соусы' but got '{sauces_header_text}'"

    # Клик "Булки" и проверка заголовка
    driver.find_element(*BUNS_TAB).click()
    buns_header_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BUNS_HEADER))
    buns_header_text = buns_header_element.text
    assert buns_header_text == "Булки", f"Expected header to be 'Булки' but got '{buns_header_text}'"