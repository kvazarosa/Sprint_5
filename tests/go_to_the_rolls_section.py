from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

# Добавить явное ожидание загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")))

# Кликнуть на раздел "Соусы"
driver.find_element(By.XPATH, "//span[contains(text(), 'Соусы')]").click()

# Кликнуть на раздел "Булки"
driver.find_element(By.XPATH, "//span[contains(text(), 'Булки')]").click()

# Проверить класс до и после клика
assert 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect' != 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'

# Закрой браузер
driver.quit()
