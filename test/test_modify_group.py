from unicodedata import name
from model.group import Group
import random


def test_modify_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    old_groups = db.get_group_list()

    group = random.choice(old_groups)

    app.group.modify_group_by_id(group.id, Group(name="Patchname"))

    new_groups = db.get_group_list()

    assert sorted(old_groups, key=Contact.id_or_max) != sorted(
        new_groups, key=Contact.id_or_max)

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(
            app.group.get_group_list(), key=Group.id_or_max)
