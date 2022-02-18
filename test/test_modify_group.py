from model.group import Group
from random import randrange

def test_modify_group_name(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, Contact(first_name="Patchfirst", middle_name="Patchmiddle", last_name="Patchlast"))
    new_contacts = db.get_contact_list()
    assert old_contacts != db.get_contact_list()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)