from model.Group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Group_name_delete", "Header_delete"))
    groups_before = app.group.get_groups()
    app.group.delete_first()

    assert len(groups_before) - 1 == app.group.count()
    groups_after = app.group.get_groups()
    groups_before[0:1] = []
    assert groups_before == groups_after
