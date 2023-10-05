from random import randrange

from test.test_phones import merge_phones_like_on_home_page


def merge_emails_like_on_home_page(contact_from_edit_page):
    merged = "\n".join(filter(lambda x: x != "",
                              filter(lambda x: x is not None, [contact_from_edit_page.email, contact_from_edit_page.email2, contact_from_edit_page.email3])))
    return merged


def test_contact_info(app):
    contacts = app.contact.get_contacts()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contacts()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email == merge_emails_like_on_home_page(contact_from_edit_page)
