# -*- coding: utf-8 -*-

from model.Contact import Contact
from test.test_add_group import random_string
import pytest

test_data = [Contact(firstname="", middlename="", lastname="", nickname="",
                     title="", company="", address="", home_phone="", mobile="", work_phone="", fax_phone="", email="", email2="", email3="",
                     secondary_phone="")] + [
                Contact(firstname=random_string("name", 10), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20),
                        nickname=random_string("nickname", 20),
                        title=random_string("title", 20), company=random_string("company", 20), address=random_string("address", 20),
                        home_phone=random_string("home_phone", 20),
                        mobile=random_string("mobile", 20), work_phone=random_string("work_phone", 20), fax_phone=random_string("fax_phone", 20),
                        email=random_string("email", 20),
                        email2=random_string("email2", 20), email3=random_string("email3", 20), secondary_phone=random_string("secondary_phone", 20))
                for i in range(5)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_new_contact(app, contact):
    contacts_before = app.contact.get_contacts()
    for cont in contacts_before:
        print(cont.id)
    contact = Contact("Boris", "שמגרקן", "Groen", "Boris",
                      "Director", "Compony_1", "Mosc", "8888888558", "99999",
                      "99999", "00000", "bls@1", "dfs@2", "eare@3", secondary_phone="888888")
    app.contact.create_new(contact)
    assert len(contacts_before) + 1 == app.contact.count()
    contacts_after = app.contact.get_contacts()
    contacts_before.append(contact)
    assert sorted(contacts_before, key=Contact.id_or_max) == sorted(contacts_after, key=Contact.id_or_max)
