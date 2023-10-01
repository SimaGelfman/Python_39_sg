# -*- coding: utf-8 -*-

from model.Group import Group


def test_add_group(app):
    groups_before = app.group.get_groups()
    app.group.create(Group("Group_name_1", "group_header_1", "group_footer_1"))
    groups_after = app.group.get_groups()
    assert len(groups_before) + 1 == len(groups_after)


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))
