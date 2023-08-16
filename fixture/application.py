from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome(
            executable_path=r'/Users/maximkulikov/SIMA/Learning_Python/chromedriver-mac-x64/chromedriver')
        self.wd.implicitly_wait(6000)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)





    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def go_home(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()
