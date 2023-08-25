from model.Group import Group


def test_edit_group(app):
    app.group.edit_first(Group("Group_name_edited", "group_header_edited", "group_footer_edited"))
