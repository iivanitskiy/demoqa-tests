import pytest
from utils.driver_factory import DriverFactory
from test_data.test_data_provider import TestDataProvider
from configuration.config_provider import ConfigProvider
from pages.login_page import LoginPage
from utils.logger import setup_logger

logger = setup_logger(__name__)

@pytest.fixture(scope="session")
def config():
    """Получение конфигурации из файла config.ini"""
    return ConfigProvider("configuration/test_config.ini")
      
@pytest.fixture(scope="session")
def test_data(config: ConfigProvider):
    """Получение данных из файла test_data.json"""
    provider = TestDataProvider(config.get("test_data", "filename"))
    return {"reg_firstname": provider.get("reg_firstname"), "reg_lastname": provider.get("reg_lastname"), "reg_username": provider.get("reg_username"), "reg_password": provider.get("reg_password"), "username": provider.get("username"), "password": provider.get("password")}

@pytest.fixture(scope="function")
def driver(config: ConfigProvider):
    """Фикстура для создания и закрытия драйвера"""
    logger.info(f"Creating driver for browser: {config.get('ui', 'browser_name')}")
    driver = DriverFactory.get_driver(config.get("ui", "browser_name"))
    driver.maximize_window()
    driver.implicitly_wait(int(config.get("ui", "timeout_seconds")))
    logger.info("Driver created and window maximized")

    yield driver

    logger.info("Quitting driver")
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL приложения"""
    return "https://demoqa.com"

@pytest.fixture(scope="function")
def logged_in_driver(driver, base_url, test_data):
    """Фикстура для предварительного логина пользователя"""
    logger.info("Starting login process via logged_in_driver fixture")
    driver.get(f"{base_url}/login")
    login_page = LoginPage(driver)
    logger.info(f"Logging in with username: {test_data['username']}")
    login_page.login(test_data["username"], test_data["password"])
    
    if not login_page.is_login_successful():
        logger.error("Login failed in logged_in_driver fixture")
        raise RuntimeError("Login failed in logged_in_driver fixture")
    
    logger.info("Login successful")
    yield driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Скриншот при падении теста"""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            screenshot = f"screenshots/{item.name}.png"
            logger.info(f"Test failed, saving screenshot to {screenshot}")
            driver.save_screenshot(screenshot)
            # Прикрепляем скриншот к Allure отчёту
            try:
                import allure
                allure.attach.file(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
                logger.info("Screenshot attached to Allure report")
            except ImportError:
                logger.warning("Allure not available, screenshot not attached")
