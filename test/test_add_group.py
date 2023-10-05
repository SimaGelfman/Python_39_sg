# -*- coding: utf-8 -*-


from model.Group import Group
import string
import random

import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    groups_before = app.group.get_groups()
    group = Group("Group_name_1", "group_header_1", "group_footer_1")
    app.group.create(group)
    assert len(groups_before) + 1 == app.group.count()
    groups_before.append(group)
    groups_after = app.group.get_groups()

    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
