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

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill the form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        self.change_field_value("firstname", contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        self.change_field_value("middlename", contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        self.change_field_value("lastname", contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        self.change_field_value("nickname", contact.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        self.change_field_value("company", contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        self.change_field_value("address", contact.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        self.change_field_value("mobile", contact.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
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

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        # click by edit button
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a").click()
        self.fill_contact_form(new_contact_data)
        # click by confirm button
        wd.find_element_by_xpath("//input[@name='update']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
