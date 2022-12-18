import pytest
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    return driver
