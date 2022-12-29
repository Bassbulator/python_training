# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_groups_page()
        self.init_group_creation()
        self.fill_group_form(Group(name="qwerty", header="qwerty", footer="qwerty"))
        self.submit_group_creation()
        self.return_to_groups_page()
        self.logout()

    def test_add_empty_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_groups_page()
        self.init_group_creation()
        self.fill_group_form(Group(name="", header="", footer=""))
        self.submit_group_creation()
        self.return_to_groups_page()
        self.logout()

    def open_groups_page(self):
        wd = self.wd
        # open groups page
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_link_text("groups").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def submit_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, group):
        wd = self.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def init_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("new").click()

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
