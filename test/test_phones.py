import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.home_phone == clear(contact_from_edit_page.home_phone)
    assert contact_from_home_page.mobile == clear(contact_from_edit_page.mobile)
    assert contact_from_home_page.work_phone == clear(contact_from_edit_page.work_phone)


def test_phones_on_contact_view_page(app):
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    assert contact_from_edit_page.home_phone == contact_from_view_page.home_phone
    assert contact_from_edit_page.mobile == contact_from_view_page.mobile
    assert contact_from_edit_page.work_phone == contact_from_view_page.work_phone


def clear(s):
    return re.sub("[() -]", "", s)