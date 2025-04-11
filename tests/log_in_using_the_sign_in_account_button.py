from conftest import new_login
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from urls import Urls

def test_creating_an_object(initializing_the_driver):
    driver = initializing_the_driver

    driver.get(Urls.HOME_PAGE_URL)

# Добавить явное ожидание загрузки страницы
    WebDriverWait(driver, 3).until(Locators.WAITING_FOR_THE_PAGE)

# Нажать на кнопку "Войти в аккаунт"
    driver.find_element(*Locators.CLICK_LOG_IN_TO_YOUR_ACCOUNT).click()

# Дождаться кликабельности кнопки "Войти"
    WebDriverWait(driver, 3).until(Locators.WAIT_FOR_THE_LOGIN_BUTTON)

# Ввести значение в поле 'Email'
    driver.find_element(*Locators.FIND_THE_EMAIL_FIELD).send_keys(new_login)

# Ввести значение в поле 'Пароль'
    driver.find_element(*Locators.FIND_THE_PASSWORD_FIELD).send_keys('123456789')

# Кликнуть на кнопку "Войти"
    driver.find_element(*Locators.CLICK_LOG_IN).click()

# Проверить вход по кнопке "Войти в аккаунт"
    expected_url = Urls.URL_LOGIN_PAGE
    current_url = driver.current_url
    assert current_url == expected_url
