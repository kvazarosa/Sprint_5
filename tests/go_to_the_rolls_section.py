from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

def test_creating_an_object(initializing_the_driver):
    driver = initializing_the_driver

    driver.get(Locators.HOME_PAGE_URL)

# Добавить явное ожидание загрузки страницы
    WebDriverWait(driver, 3).until(Locators.WAITING_FOR_THE_PAGE)

# Кликнуть на раздел "Соусы"
    driver.find_element(*Locators.CLICK_ON_SAUCES).click()

# Кликнуть на раздел "Булки"
    driver.find_element(*Locators.CLICK_ON_THE_ROLLS).click()

# Проверить класс до и после клика
    assert 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect' != 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'
