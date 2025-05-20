import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    return "https://qa-desk.stand.praktikum-services.ru"
