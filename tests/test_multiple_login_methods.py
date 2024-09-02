import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_main_page(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()  # клик по кнопке "Войти в аккаунт"
    login()  # Выполнение авторизации

def test_login_personal_account(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, "(//p[@class='AppHeader_header__linkText__3q_va ml-2'])[3]").click()  # клик по кнопке "Личный кабинет"
    login()  # Выполнение авторизации

def test_login_registration_page(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj']").click()  # клик по гиперссылке "Войти"
    login()  # Выполнение авторизации

def test_login_forgot_password(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj']").click()  # клик по гиперссылке "Войти"
    login()  # Выполнение авторизации

# fortest

