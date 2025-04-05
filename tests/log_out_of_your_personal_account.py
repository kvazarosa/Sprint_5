from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

# Добавить явное ожидание загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")))

# Нажать на кнопку "Войти в аккаунт"
driver.find_element(By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg").click()

# Дождаться кликабельности кнопки "Войти"
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]")))

Email = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
# Ввести значение в поле 'Email'
Email.send_keys('jenya_chabanov_20_111@yandex.ru')

Password = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
# Ввести значение в поле 'Пароль'
Password.send_keys('123456789')

# Кликнуть на кнопку "Войти"
driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()

# Дождаться загрузки главной страницы
WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))

# Нажать на кнопку "Личный кабинет"
driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()

# Дождаться кликабельности кнопки "Выход"
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Выход')]")))

# Кликнуть на кнопку "Выход"
driver.find_element(By.XPATH, "//button[contains(text(), 'Выход')]").click()

# Дождаться кликабельности кнопки "Лента заказов"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]")))

# Проверить выход из личного кабинета
assert (WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Вход')]"))).is_displayed())

# Закрой браузер
driver.quit()
