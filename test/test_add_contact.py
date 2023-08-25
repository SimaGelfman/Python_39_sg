# -*- coding: utf-8 -*-

from model.Contact import Contact


def test_add_new_contact(app):
    app.contact.create_new(Contact("Boris", "Vlad", "Groen", "Boris",
                                   "Director", "Compony_1", "Mosc", "888888", "99999",
                                   "99999", "00000", "bls"))


def test_add_empty_contact(app):
    app.contact.create_new(Contact("", "", "", "", "", "", "", "", "",
                                   "", "", ""))
