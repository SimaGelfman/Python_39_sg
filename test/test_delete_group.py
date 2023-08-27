from model.Group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Group_name_delete", "Header_delete"))
    app.group.delete_first()