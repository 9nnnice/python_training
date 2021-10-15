from selenium.webdriver.firefox.webdriver import WebDriver

class Helper:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)