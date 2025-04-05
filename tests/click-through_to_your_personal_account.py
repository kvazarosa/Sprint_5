from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

# Добавить явное ожидание загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")))

# Нажать на кнопку "Личный кабинет"
driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()

# Дождаться кликабельности кнопки "Войти"
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]")))


# Проверить открытие личного кабинета
expected_url = "https://stellarburgers.nomoreparties.site/login"
current_url = driver.current_url
assert current_url == expected_url

# Закрой браузер
driver.quit()
