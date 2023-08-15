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
    app.login(login="admin", password="secret")

    app.add_group(Group("Group_name_1", "group_header_1", "group_footer_1"))

    app.logout()


def test_add_empty_group(app):
    app.login(login="admin", password="secret")

    app.add_group(Group("", "", ""))

    app.logout()
