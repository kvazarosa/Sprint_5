from selenium.webdriver.support.wait import WebDriverWait
from conftest import new_login
from locators import Locators


def test_creating_an_object(initializing_the_driver):
    driver = initializing_the_driver

    driver.get(Locators.HOME_PAGE_URL)

# Добавить явное ожидание загрузки страницы
    WebDriverWait(driver, 3).until(Locators.WAITING_FOR_THE_PAGE)

# Нажать на кнопку "Войти в аккаунт"
    driver.find_element(*Locators.CLICK_LOG_IN_TO_YOUR_ACCOUNT).click()

# Дождаться текст "Зарегистрироваться"
    WebDriverWait(driver, 3).until(Locators.WEIT_FOR_THE_TEXT_TO_REGISTER)

# Нажать на текст "Зарегистрироваться"
    driver.find_element(*Locators.CLICK_ON_THE_SIGN_UP_TEXT).click()

# Дождаться поля "Имя"
    WebDriverWait(driver, 3).until(Locators.WAIT_FOR_THE_NAME_FIELD)

# Ввести значение в поле 'Имя'
    driver.find_element(*Locators.FIND_THE_NAME_FIELD).send_keys('Женя')

# Ввести значение в поле 'Email'
    driver.find_element(*Locators.FIND_THE_EMAIL_FIELD).send_keys(new_login)

# Ввести значение в поле 'Пароль'
    driver.find_element(*Locators.FIND_THE_PASSWORD_FIELD).send_keys('123456789')

# Кликнуть на кнопку "Зарегистрироваться"
    driver.find_element(*Locators.CLICK_ON_REGISTER).click()

# Дождаться загрузки страницы регистрации
    WebDriverWait(driver, 3).until(Locators.WAIT_FOR_THE_REGISTRATION_PAGE)

# Проверить успешную регистрацию
    expected_url = Locators.URL_LOGIN_PAGE
    current_url = driver.current_url
    assert current_url == expected_url
