import random
import pytest
from selenium import webdriver

new_login = f"jenya_chabanov_20_{random.randint(100, 999)}@yandex.ru"


@pytest.fixture
def initializing_the_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
