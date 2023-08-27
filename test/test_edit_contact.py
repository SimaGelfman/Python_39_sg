from model.Contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact("Br_delet, Vl_delete"))
    app.contact.edit_first(Contact("Br_edit", "Vlad_edit", "Groen_edit", "Boris_edit",
                                   "Director_edit", "Compony_1_edit", "Mosc_edit", "888888_edit", "999993",
                                   "999993", "000003", "bls_edit"))
