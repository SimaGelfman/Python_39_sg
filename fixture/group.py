class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def change_field_value(self, text_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(text_field_name).click()
            wd.find_element_by_name(text_field_name).clear()
            wd.find_element_by_name(text_field_name).send_keys(text)

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.get("http://localhost/addressbook/group.php")

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def select_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
