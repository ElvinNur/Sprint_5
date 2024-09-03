import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

def test_login_main_page(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*MAIN_PAGE_LOGIN_BUTTON).click()  # клик по кнопке "Войти в аккаунт"
    login()  # Выполнение авторизации

def test_login_personal_account(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()  # клик по кнопке "Личный кабинет"
    login()  # Выполнение авторизации

def test_login_registration_page(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*REGISTRATION_PAGE_LOGIN_LINK).click()  # клик по гиперссылке "Войти"
    login()  # Выполнение авторизации

def test_login_forgot_password(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(*FORGOT_PASSWORD_PAGE_LOGIN_LINK).click()  # клик по гиперссылке "Войти"
    login()  # Выполнение авторизации

