from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import new_login
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

# Добавить явное ожидание загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")))

# Нажать на кнопку "Войти в аккаунт"
driver.find_element(By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg").click()

# Дождаться текст "Зарегистрироваться"
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'Auth_link__1fOlj')))

# Нажать на текст "Зарегистрироваться"
driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()

# Дождаться поля "Имя"
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "//label[contains(@class, 'input__placeholder') and contains(@class, 'text') and contains(@class, 'noselect') and contains(@class, 'text_type_main-default') and text()='Имя']")))

Name = driver.find_element(By.CSS_SELECTOR, "div.input > input[name='name']")
# Ввести значение в поле 'Имя'
Name.send_keys('Женя')

Email = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
# Ввести значение в поле 'Email'
Email.send_keys(new_login)

Password = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
# Ввести значение в поле 'Пароль'
Password.send_keys('123')

# Сохранить значение пароля
entered_password = Password.get_attribute('value')

# Кликнуть на кнопку "Зарегистрироваться"
driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click()

# Дождаться загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.url_contains("/login"))

# Пароль меньше 6 символов
assert len(entered_password) > 5


# Закрой браузер
driver.quit()
