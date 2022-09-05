from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.firefox import GeckoDriverManager


class DriverTool:
    def __init__(self):
        self.drivers = []

    def startup(self, browser, options=None, profile=None):
        browser = browser.lower()
        match browser:
            case 'chrome':
                if options is not None:
                    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
                    self.drivers.append(driver)
                    return driver
                else:
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                    self.drivers.append(driver)
                    return driver
            case 'firefox':
                if profile is not None:
                    driver = webdriver.Firefox(executable_path=(GeckoDriverManager().install()),
                                               firefox_profile=profile)
                    self.drivers.append(driver)
                    return driver
                else:
                    driver = webdriver.Firefox(executable_path=(GeckoDriverManager().install()))
                    self.drivers.append(driver)
                    return driver

    def close_all(self):
        for d in self.drivers:
            d.quit()
