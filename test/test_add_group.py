# -*- coding: utf-8 -*-


from model.Group import Group


def test_add_group(app):
    groups_before = app.group.get_groups()
    group = Group("Group_name_1", "group_header_1", "group_footer_1")
    app.group.create(group)
    assert len(groups_before) + 1 == app.group.count()
    groups_before.append(group)
    groups_after = app.group.get_groups()

    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)


