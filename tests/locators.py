from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

class Locators():
    CLICK_LOG_IN_TO_YOUR_ACCOUNT = (By.CLASS_NAME,
                      "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")  # Нажать на кнопку "Войти в аккаунт"
    CLICK_ON_REGISTER = (By.CSS_SELECTOR,
                "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")  # Кликнуть на кнопку "Зарегистрироваться"
    CLICK_ON_YOUR_PERSONAL_ACCOUNT = (By.XPATH,
                "//p[contains(text(), 'Личный Кабинет')]") # Нажать на кнопку "Личный кабинет"
    CLICK_LOG_IN = (By.XPATH,
                "//a[contains(text(), 'Войти')]")  # Кликнуть на кнопку "Войти"
    FIND_THE_NAME_FIELD = (By.CSS_SELECTOR, "div.input > input[name='name']")  # Найти поле "Имя"
    FIND_THE_EMAIL_FIELD = (By.XPATH,
                "//label[text()='Email']/following-sibling::input")  # Найти поле "Email"
    FIND_THE_PASSWORD_FIELD = (By.XPATH,
                "//label[text()='Пароль']/following-sibling::input")  # Найти поле "Password"
    WAIT_FOR_THE_REGISTRATION_PAGE = (
            expected_conditions.url_contains("/login"))  # Дождаться загрузки страницы регистрации
    WAITING_FOR_THE_PAGE = (expected_conditions.element_to_be_clickable((By.CLASS_NAME,
                      "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")))  # Добавить явное ожидание загрузки главной страницы
    WAIT_FOR_THE_LOGIN_BUTTON = (expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Войти')]")))  # Дождаться кликабельности кнопки "Войти"
