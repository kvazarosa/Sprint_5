from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import new_login
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

# Нажать на кнопку "Личный кабинет"
    driver.find_element(*Locators.CLICK_ON_YOUR_PERSONAL_ACCOUNT).click()

# Дождаться кликабельности кнопки "Лента заказов"
    WebDriverWait(driver, 3).until(Locators.WAIT_CLICKABILITY_ORDER_BUTTON)

# Проверить выход из личного кабинета
    assert (WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Вход')]"))).is_displayed())
