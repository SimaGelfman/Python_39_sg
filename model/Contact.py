from sys import maxsize


class Contact:
    def __init__(self, firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                 home_phone="", mobile="", work_phone="", fax_phone="", email="", email2="", email3="",
                 secondary_phone="", all_phones_from_home_page=None, all_email=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile = mobile
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.secondary_phone = secondary_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email = all_email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return self.id is None or other.id is None or self.id == other.id and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(contact):
        if contact.id:
            return int(contact.id)
        else:
            return maxsize
