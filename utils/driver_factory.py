from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser_name="chrome", headless=False):
        if browser_name.lower() == "chrome":
            options = Options()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            return webdriver.Chrome(
                service=webdriver.chrome.service.Service(
                    ChromeDriverManager().install()
                ),
                options=options,
            )

        elif browser_name.lower() == "firefox":
            return webdriver.Firefox(
                service=webdriver.firefox.service.Service(
                    GeckoDriverManager().install()
                )
            )
        else:
            raise ValueError(f"Browser {browser_name} not supported")
