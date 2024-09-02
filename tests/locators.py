from selenium.webdriver.common.by import By

# Локаторы для страницы регистрации
REGISTER_NAME_INPUT = (By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]")
REGISTER_EMAIL_INPUT = (By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]")
REGISTER_PASSWORD_INPUT = (By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[3]")
REGISTER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']")
LOGIN_BUTTON_ON_REGISTER_PAGE = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # кнопка "Войти" на странице регистрации

# Локаторы для страницы входа (авторизации)
LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "(//p[@class='AppHeader_header__linkText__3q_va ml-2'])[3]")

# Локаторы для главной страницы
MAIN_PAGE_LOGIN_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

# Локаторы для страницы регистрации
REGISTRATION_PAGE_LOGIN_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj']")

# Локаторы для страницы восстановления пароля
FORGOT_PASSWORD_PAGE_LOGIN_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj']")

# Локаторы для страницы личного кабинета
LOGOUT_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button")
PERSONAL_ACCOUNT_PAGE_HEADER = (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']")  # Новый локатор для текста на странице личного кабинета

# Локатор для проверки перехода на страницу "Вход"
LOGIN_PAGE_HEADER = (By.CSS_SELECTOR, "#root > div > main > div > h2")

# Локаторы для "Конструктор" и "Логотип"
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
BURGER_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
LOGO_BUTTON = (By.CSS_SELECTOR, "#root > div > header > nav > div > a > svg")

# Локаторы для разделов "Начинки", "Соусы", "Булки"
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
BUNS_TAB = (By.XPATH, "//span[text()='Булки']")

# Локаторы для заголовков разделов "Начинки", "Соусы", "Булки"
FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")
SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")
BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")
