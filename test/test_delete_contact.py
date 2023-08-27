from model.Contact import Contact


def test_add_new_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact("Boris_delete", "Vlad_delete", "Groen_delete", "Boris_delete"))
    app.contact.delete_first()

