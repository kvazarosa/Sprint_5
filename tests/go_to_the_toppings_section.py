from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from urls import Urls

def test_creating_an_object(initializing_the_driver):
    driver = initializing_the_driver

    driver.get(Urls.HOME_PAGE_URL)

# Добавить явное ожидание загрузки страницы
    WebDriverWait(driver, 3).until(Locators.WAITING_FOR_THE_PAGE)

# Кликнуть на раздел "Начинки"
    driver.find_element(*Locators.CLICK_ON_THE_TOPPINGS).click()

# Сохраняем элемент, у которого нужно проверить классы
    element = driver.find_element(*Locators.CLICK_ON_THE_TOPPINGS)

# Получаем значение атрибута class
    classes = element.get_attribute('class')

# Проверяем, содержит ли строка класса 'type_current'
    assert 'type_current' not in classes