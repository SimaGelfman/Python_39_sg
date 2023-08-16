# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.Group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(login="admin", password="secret")

    app.group.create(Group("Group_name_1", "group_header_1", "group_footer_1"))

    app.session.logout()


def test_add_empty_group(app):
    app.session.login(login="admin", password="secret")

    app.group.create(Group("", "", ""))

    app.session.logout()
