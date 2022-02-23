from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        db.create(Group(name="test"))

    old_groups = db.get_group_list()

    group = random.choice(old_groups)

    app.group.delete_group_by_id(group.id)

    new_groups = db.get_group_list()

    assert len(old_groups) - 1 == len(new_groups)

    filtered = [i for i in old_contacts if i.id == contact.id]

    assert sorted(filtered, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max)

    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(
            app.group.get_group_list(), key=Group.id_or_max)
