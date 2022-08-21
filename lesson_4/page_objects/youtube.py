from selenium.webdriver import Keys
from seleniumpagefactory import PageFactory


class YouTube(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "masthead":("id","masthead-container"),
        "searchBar": ("id", "search"),
        "searchButton": ("id", "search-icon-legacy"),
        "firstResult": ("xpath", "(//yt-formatted-string[@class = 'style-scope ytd-video-renderer'])[1]"),
    }

    def search_video(self,text):
        self.driver.get("https://www.youtube.com/results?search_query="+text)
        # self.masthead.click()
        # self.searchBar.set_text(text)
        # self.searchButton.click()
        return self.firstResult.get_text()