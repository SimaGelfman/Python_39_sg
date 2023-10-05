import re

from model.Contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("phone2", contact.secondary_phone)

    def create_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.go_home()
        self.contacts_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.go_home()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.go_home()
        self.contacts_cache = None

    def delete_first(self):
        self.delete_contact_by_index(0)

    def edit_first(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.app.go_home()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.app.go_home()
        self.contacts_cache = None

    def count(self):
        wd = self.app.wd
        self.app.go_home()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contacts(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.go_home()
            self.contacts_cache = []
            contact_table = wd.find_element_by_id("maintable")
            for row in contact_table.find_elements_by_css_selector('tr')[1:]:
                id = row.find_element_by_css_selector('input[type="checkbox"]').get_attribute('id')
                cells = row.find_elements_by_css_selector('td')
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contacts_cache.append(Contact(firstname=first_name, lastname=last_name, address=address, all_email=all_email,
                                                   id=id, all_phones_from_home_page=all_phones))
        return self.contacts_cache

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.go_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_css_selector('td')[7]
        cell.find_element_by_css_selector('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.go_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_css_selector('td')[6]
        cell.find_element_by_css_selector('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        fax_phone = wd.find_element_by_name("fax").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, home_phone=home_phone, mobile=mobile,
                       work_phone=work_phone, fax_phone=fax_phone,email=email, email2=email2, email3=email3, secondary_phone=secondary_phone)

    def change_field_value(self, text_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(text_field_name).click()
            wd.find_element_by_name(text_field_name).clear()
            wd.find_element_by_name(text_field_name).send_keys(text)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        fax_phone = re.search("F: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile=mobile, work_phone=work_phone, fax_phone=fax_phone)
