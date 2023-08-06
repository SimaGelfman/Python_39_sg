# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestCreateNewGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(
            executable_path=r'/Users/maximkulikov/SIMA/Learning_Python/chromedriver-mac-x64/chromedriver')
        self.wd.implicitly_wait(6000)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, admin="admin", secret="secret")
        self.open_groups_page(wd)

        self.add_group(wd, group_name="Group_name_1", group_header="group_header_1", group_footer="group_footer_1")
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def add_group(self, wd, group_name, group_header, group_footer):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group_footer)
        wd.find_element_by_name("submit").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()
        wd.get("http://localhost/addressbook/group.php")

    def login(self, wd, admin, secret):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(admin)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(secret)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()