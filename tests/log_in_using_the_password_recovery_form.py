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

# Дождаться текст "Восстановить пароль"
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")))

# Нажать на текст "Восстановить пароль"
driver.find_element(By.XPATH, "//a[contains(text(), 'Восстановить пароль')]").click()

# Дождаться кликабельности текста "Войти"
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Войти')]")))

# Кликнуть на текст "Войти"
driver.find_element(By.XPATH, "//a[contains(text(), 'Войти')]").click()

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

# Проверить вход по кнопке "Личный Кабинет"
expected_url = "https://stellarburgers.nomoreparties.site/"
current_url = driver.current_url
assert current_url == expected_url

# Закрой браузер
driver.quit()
