import pytest
from utils.driver_factory import DriverFactory
from test_data.test_data_provider import TestDataProvider
from configuration.config_provider import ConfigProvider

@pytest.fixture(scope="session")
def config():
    """Получение конфигурации из файла config.ini"""
    return ConfigProvider("configuration/test_config.ini")
     
@pytest.fixture(scope="session")
def test_data(config: ConfigProvider):
    """Получение данных из файла test_data.json"""
    provider = TestDataProvider(config.get("test_data", "filename"))
    return {"username": provider.get("username"), "password": provider.get("password")}

@pytest.fixture(scope="function")
def driver(config: ConfigProvider):
    """Фикстура для создания и закрытия драйвера"""
    driver = DriverFactory.get_driver(config.get("ui", "browser_name"))
    driver.maximize_window()
    driver.implicitly_wait(int(config.get("ui", "timeout_seconds")))

    yield driver

    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL приложения"""
    return "https://demoqa.com"

# def db(config: ConfigProvider):
#     """Подключение к базе данных"""
#     return config.get_db_connection_string

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Скриншот при падении теста"""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            screenshot = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot)
