from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory


class GoogleTranslate(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "dropdown": ("xpath", "(//span[@class='zQ0atf'])[1]"),
        "hebrew": ("xpath", "(//div[@class='Llmcnf'][contains(text(),'Hebrew')])[1]"),
        "textBox": ("xpath", "//textarea"),
        "result": ("css", "[class='Q4iAWc']")
    }

    def translate_text(self, text):

        self.textBox.clear_text()
        self.textBox.set_text(text)
        return self.result.get_text()

