# -*- coding: utf-8 -*-

from model.Contact import Contact


def test_add_new_contact(app):
    contacts_before = app.contact.get_contacts()
    for cont in contacts_before:
        print(cont.id)
    contact = Contact("Boris", "Vlad", "Groen", "Boris",
                                   "Director", "Compony_1", "Mosc", "888888", "99999",
                                   "99999", "00000", "bls")
    app.contact.create_new(contact)
    contacts_after = app.contact.get_contacts()
    assert len(contacts_before) + 1 == len(contacts_after)
    contacts_before.append(contact)
    assert sorted(contacts_before, key=Contact.id_or_max) == sorted(contacts_after, key=Contact.id_or_max)



def test_add_empty_contact(app):
    contacts_before = app.contact.get_contacts()
    contact = Contact("", "", "", "", "", "", "", "", "",
                                   "", "", "")
    app.contact.create_new(contact)
    contacts_after = app.contact.get_contacts()
    assert len(contacts_before) + 1 == len(contacts_after)
    contacts_before.append(contact)
    assert sorted(contacts_before, key=Contact.id_or_max) == sorted(contacts_after, key=Contact.id_or_max)
