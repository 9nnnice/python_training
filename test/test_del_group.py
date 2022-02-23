from model.group import Group
from time import sleep
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        db.create(Group(name="test"))

    old_groups = db.get_group_list()

    group = random.choice(old_groups)

    app.group.delete_group_by_id(group.id)

    sleep(1)  # Ждем пока из удалится запись?

    new_groups = db.get_group_list()

    assert len(old_groups) - 1 == len(new_groups)

    old_groups.remove(group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max)

    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(
            app.group.get_group_list(), key=Group.id_or_max)
