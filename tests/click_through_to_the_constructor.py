from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

def test_creating_an_object(initializing_the_driver):
    driver = initializing_the_driver

    driver.get(Locators.HOME_PAGE_URL)

# Добавить явное ожидание загрузки страницы
    WebDriverWait(driver, 3).until(Locators.WAITING_FOR_THE_PAGE)

# Нажать на кнопку "Личный кабинет"
    driver.find_element(*Locators.CLICK_ON_YOUR_PERSONAL_ACCOUNT).click()

# Дождаться кликабельности кнопки "Войти"
    WebDriverWait(driver, 3).until(Locators.WAIT_FOR_THE_LOGIN_BUTTON)

# Нажать на кнопку "Конструктор"
    driver.find_element(*Locators.CLICK_ON_THE_CONSTRUCTOR).click()

# Добавить явное ожидание загрузки страницы
    WebDriverWait(driver, 3).until(Locators.WAITING_FOR_THE_PAGE)

# Проверить открытие главной страницы
    expected_url = Locators.HOME_PAGE_URL
    current_url = driver.current_url
    assert current_url == expected_url
