import time

from selenium import webdriver
from selenium.webdriver import Keys, FirefoxProfile
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from lesson_4.page_objects.google_translate import GoogleTranslate
from lesson_4.page_objects.youtube import YouTube
from lesson_4.utils.selenium_startup import DriverTool

driver = DriverTool()
driver_chrome = driver.startup('chrome')
driver_firefox = driver.startup('firefox')
# question 1
driver_chrome.get('http://www.walla.co.il')
driver_firefox.get('http://www.ynet.co.il')

time.sleep(5)

# question 2

title = driver_chrome.title
driver_chrome.refresh()
assert title == driver_chrome.title

# question 4
driver_chrome.maximize_window()
driver_chrome.get('https://translate.google.com/')
translate = GoogleTranslate(driver_chrome)
print(translate.translate_text("שלום לכולם. אתם נהנים בשיעור?  "))

# question 5

print(YouTube(driver_chrome).search_video("five to one"))

# question 8

driver_chrome.delete_all_cookies()
print(driver_chrome.get_cookies())

# question 9

driver_chrome.get("https://github.com")
search = driver_chrome.find_element(By.XPATH, "//input[@data-test-selector='nav-search-input']")
search.send_keys("selenium")
search.send_keys(Keys.ENTER)

# question 10
options_chrome = Options()
options_chrome.add_argument("--disable-extensions")
new_chrome = driver.startup('chrome', options_chrome)
profile = webdriver.FirefoxProfile()
new_firefox = driver.startup('firefox',profile)

driver.close_all()
