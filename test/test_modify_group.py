from unicodedata import name
from model.group import Group
import random


def test_modify_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    old_groups = db.get_group_list()

    group = random.choice(old_groups)

    new_group = Group(id=group.id, name="Patchname")

    app.group.modify_group_by_id(new_group.id, new_group)

    new_groups = db.get_group_list()

    index = old_groups.index(group)

    old_groups[index] = new_group

    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max)

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(
            app.group.get_group_list(), key=Group.id_or_max)
