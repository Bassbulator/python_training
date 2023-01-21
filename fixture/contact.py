from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contact):
        wd = self.app.wd
        # Click by link "add new"
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # click by "enter" button
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_homepage()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill the form
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_xpath("//select[@name='bday']")).select_by_visible_text("9")
        wd.find_element_by_xpath("//option[@value='9']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_xpath("//select[@name='bmonth']")).select_by_visible_text("November")
        wd.find_element_by_xpath("//option[@value='November']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1999")

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # choose group
        wd.find_element_by_name("selected[]").click()
        # confirm delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept alert OK
        Alert(wd).accept()
        self.return_homepage()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        # click by edit button
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr/td/a").click()
        self.fill_contact_form(new_contact_data)
        # click by confirm button
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.return_homepage()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
        return len(wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[]/td[]/a"))