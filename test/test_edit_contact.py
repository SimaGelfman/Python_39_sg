from model.Contact import Contact


def test_add_new_contact(app):
    app.session.login(login="admin", password="secret")

    app.contact.edit_first(Contact("Br_edit", "Vlad_edit", "Groen_edit", "Boris_edit",
                                   "Director_edit", "Compony_1_edit", "Mosc_edit", "888888_edit", "999993",
                                   "999993", "000003", "bls_edit"))

    app.session.logout()