from model.Group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Group_name_delete", "Header_delete"))
    app.group.edit_first(Group("Group_name_edited", "group_header_edited", "group_footer_edited"))
