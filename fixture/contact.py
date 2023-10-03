from model.Contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)

        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)

    def create_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.go_home()
        self.contacts_cache = None

    def delete_first(self):
        wd = self.app.wd
        self.app.go_home()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.go_home()
        self.contacts_cache = None

    def edit_first(self, contact):
        wd = self.app.wd
        self.app.go_home()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
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
                self.contacts_cache.append(Contact(firstname=first_name, lastname=last_name, address=address, id=id))
        return self.contacts_cache

