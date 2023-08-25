# -*- coding: utf-8 -*-

from model.Group import Group


def test_add_group(app):
    app.group.create(Group("Group_name_1", "group_header_1", "group_footer_1"))


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))
