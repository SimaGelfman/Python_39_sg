# -*- coding: utf-8 -*-
from application import Application
from Contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):

    app.login(login="admin", password="secret")

    app.create_new_contact(Contact("Boris", "Vlad", "Groen", "Boris",
                                        "Director", "Compony_1", "Mosc", "888888", "99999",
                                        "99999", "00000", "bls"))

    app.logout()

def test_add_empty_contact(app):

   app.login(login="admin", password="secret")

   app.create_new_contact(Contact("", "", "", "","", "", "", "", "",
                                        "", "", ""))

   app.logout()











