from model.Contact import Contact


def test_delete_contact(app):
    contacts_before = app.contact.get_contacts()
    if app.contact.count() == 0:
        app.contact.create_new(Contact("Boris_delete", "Vlad_delete", "Groen_delete", "Boris_delete"))
    app.contact.delete_first()
    contacts_after = app.contact.get_contacts()
    assert len(contacts_before) - 1 == len(contacts_after)
    contacts_before[0:1] = []
    assert contacts_before == contacts_after



