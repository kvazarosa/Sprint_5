from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class Locators():
    CLICK_LOG_IN_TO_YOUR_ACCOUNT = (By.CLASS_NAME,
                      "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")  # Нажать на кнопку "Войти в аккаунт"
    CLICK_ON_REGISTER = (By.CSS_SELECTOR,
                "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")  # Кликнуть на кнопку "Зарегистрироваться"
    CLICK_ON_YOUR_PERSONAL_ACCOUNT = (By.XPATH,
                "//p[contains(text(), 'Личный Кабинет')]") # Нажать на кнопку "Личный кабинет"
    CLICK_LOG_IN = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")  # Кликнуть на кнопку "Войти"
    CLICK_ON_THE_SIGN_UP_TEXT = (By.CLASS_NAME, 'Auth_link__1fOlj') # Нажать на текст "Зарегистрироваться"
    CLICK_IN_STELLAR = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Нажать на лого "stellar burgers"
    CLICK_ON_THE_CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]") # Нажать на кнопку "Конструктор"
    CLICK_ON_SAUCES = (By.XPATH, "//span[contains(text(), 'Соусы')]") # Кликнуть на раздел "Соусы"
    CLICK_ON_THE_ROLLS = (By.XPATH, "//span[contains(text(), 'Булки')]") # Кликнуть на раздел "Булки"
    CLICK_ON_THE_TOPPINGS = (By.XPATH, "//span[contains(text(), 'Начинки')]") # Кликнуть на раздел "Начинки"
    CLICK_TEXT_RESTORE_PASSWORD = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]") # Нажать на текст "Восстановить пароль"
    CLICK_ON_LOGIN_TEXT = (By.XPATH, "//a[contains(text(), 'Войти')]") # Кликнуть на текст "Войти"
    CLICK_ON_EXIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]") # Кликнуть на кнопку "Выход"
    EXIT = (By.XPATH, "//button[@class='Account_button__14Yp3' and contains(text(), 'Выход')]")


    FIND_THE_NAME_FIELD = (By.CSS_SELECTOR, "div.input > input[name='name']")  # Найти поле "Имя"
    FIND_THE_EMAIL_FIELD = (By.XPATH,
                "//label[text()='Email']/following-sibling::input")  # Найти поле "Email"
    FIND_THE_PASSWORD_FIELD = (By.XPATH,
                "//label[text()='Пароль']/following-sibling::input")  # Найти поле "Password"


    WAIT_FOR_THE_REGISTRATION_PAGE = (expected_conditions.url_contains("/login"))  # Дождаться загрузки страницы регистрации
    WAITING_FOR_THE_PAGE = (expected_conditions.element_to_be_clickable((By.CLASS_NAME,
                      "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")))  # Добавить явное ожидание загрузки главной страницы
    WAIT_FOR_THE_LOGIN_BUTTON = (expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Войти')]")))  # Дождаться кликабельности кнопки "Войти"
    WEIT_FOR_THE_TEXT_TO_REGISTER = (expected_conditions.element_to_be_clickable(
            (By.CLASS_NAME, 'Auth_link__1fOlj'))) # Дождаться текст "Зарегистрироваться"
    WAIT_FOR_THE_NAME_FIELD = (expected_conditions.element_to_be_clickable(
            (By.XPATH, "//label[contains(@class, 'input__placeholder') and contains(@class, 'text') and contains(@class, 'noselect') and contains(@class, 'text_type_main-default') and text()='Имя']"))) # Дождаться поля "Имя"
    WAIT_TEXT_RECOVER_PASSWORD = (expected_conditions.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]"))) # Дождаться текст "Восстановить пароль"
    WAIT_TEXT_CLICKABLE_LOGIN = (expected_conditions.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(), 'Войти')]"))) # Дождаться кликабельности текста "Войти"
    WAIT_EXIT_BUTTON_CLICKABLE = (expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Выход')]"))) # Дождаться кликабельности кнопки "Выход"
    WAIT_CLICKABILITY_ORDER_BUTTON = (expected_conditions.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(), 'Вход')]"))) # Дождаться кликабельности кнопки "Лента заказов"
