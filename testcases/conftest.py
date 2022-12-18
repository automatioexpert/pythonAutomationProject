import pytest
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.implicitly_wait(10)
    elif browser == 'firefox':
        driver=webdriver.Firefox(GeckoDriverManager().install())
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.implicitly_wait(10)
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.implicitly_wait(10)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/Hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########PYTEST HTML REPORT########################
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)