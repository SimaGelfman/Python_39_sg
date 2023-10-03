from random import randrange

from model.Group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Group_name_delete", "Header_delete"))
    groups_before = app.group.get_groups()
    index = randrange(len(groups_before))
    group = Group("Group_name_edited", "group_header_edited", "group_footer_edited")
    group.id = groups_before[index].id
    app.group.edit_group_by_index(index, group)
    groups_after = app.group.get_groups()
    groups_before[index] = group
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
