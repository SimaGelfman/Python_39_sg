from model.Contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact("Br_delet, Vl_delete"))
    contacts_before = app.contact.get_contacts()
    contact = Contact("Boris_edited", lastname="Vlad_edited")
    contact.id = contacts_before[0].id
    app.contact.edit_first(contact)

    len(contacts_before) == app.contact.count()
    contacts_after = app.contact.get_contacts()
    contacts_before[0] = contact
    assert sorted(contacts_before, key=Contact.id_or_max) == sorted(contacts_after, key=Contact.id_or_max)
