from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, browser, base_url):
        chrome_driver_path = '/Users/sima.gelfman/github/chromedriver-mac-arm64/chromedriver'
        if browser == "chrome":
            self.wd = webdriver.Chrome(executable_path=chrome_driver_path)
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "safari":
            self.wd = webdriver.Safari()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.base_url = base_url
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def go_home(self):
        wd = self.wd
        if not (wd.current_url.endswith("/index.php") and wd.find_elements_by_link_text("link=Last name")):
            wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()
