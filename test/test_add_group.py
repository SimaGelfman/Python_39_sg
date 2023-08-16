# -*- coding: utf-8 -*-

from model.Group import Group


def test_add_group(app):
    app.session.login(login="admin", password="secret")

    app.group.create(Group("Group_name_1", "group_header_1", "group_footer_1"))

    app.session.logout()


def test_add_empty_group(app):
    app.session.login(login="admin", password="secret")

    app.group.create(Group("", "", ""))

    app.session.logout()
