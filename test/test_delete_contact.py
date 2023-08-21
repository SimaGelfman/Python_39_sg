from model.Contact import Contact


def test_add_new_contact(app):
    app.session.login(login="admin", password="secret")

    app.contact.delete_first()

    app.session.logout()