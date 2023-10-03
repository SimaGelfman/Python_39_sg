from random import randrange

from model.Contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact("Boris_delete", "Vlad_delete", "Groen_delete", "Boris_delete"))
    contacts_before = app.contact.get_contacts()
    index = randrange(len(contacts_before))
    app.contact.delete_contact_by_index(index)
    assert len(contacts_before) - 1 == app.contact.count()
    contacts_after = app.contact.get_contacts()
    contacts_before[index:index + 1] = []
    assert contacts_before == contacts_after



