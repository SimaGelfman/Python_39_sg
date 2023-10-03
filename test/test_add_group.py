# -*- coding: utf-8 -*-


from model.Group import Group


def test_add_group(app):
    groups_before = app.group.get_groups()
    group = Group("Group_name_1", "group_header_1", "group_footer_1")
    app.group.create(group)
    groups_after = app.group.get_groups()
    assert len(groups_before) + 1 == len(groups_after)
    groups_before.append(group)

    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)


def test_add_empty_group(app):
    groups_before = app.group.get_groups()
    group = Group("", "", "")
    app.group.create(group)
    groups_after = app.group.get_groups()
    assert len(groups_before) + 1 == len(groups_after)
    groups_before.append(group)
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
