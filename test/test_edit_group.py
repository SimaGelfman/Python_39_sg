from model.Group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Group_name_delete", "Header_delete"))
    groups_before = app.group.get_groups()
    group = Group("Group_name_edited", "group_header_edited", "group_footer_edited")
    group.id = groups_before[0].id
    app.group.edit_first(group)
    groups_after = app.group.get_groups()
    groups_before[0] = group
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
