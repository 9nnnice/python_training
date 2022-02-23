# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, check_ui, json_groups):
    group = json_groups

    old_groups = db.get_group_list()
    old_groups.append(group)

    app.group.create(group)

    new_groups = db.get_group_list()

    assert len(old_groups) + 1 == len(new_groups)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max)

    if check_ui:
        sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(
            new_groups, key=Group.id_or_max)
