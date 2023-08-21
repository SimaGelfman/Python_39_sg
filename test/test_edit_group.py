from model.Group import Group


def test_edit_group(app):
    app.session.login(login="admin", password="secret")

    app.group.edit_first(Group("Group_name_edited", "group_header_edited", "group_footer_edited"))

    app.session.logout()