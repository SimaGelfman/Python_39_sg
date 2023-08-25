from model.Contact import Contact


def test_add_new_contact(app):
    app.contact.delete_first()

