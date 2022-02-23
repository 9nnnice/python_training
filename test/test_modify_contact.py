import random

from model.contact import Contact
from random import randrange
from time import sleep


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test"))

    old_contacts = db.get_contact_list()

    contact = random.choice(old_contacts)

    app.contact.modify_contact_by_id(contact.id, Contact(
        first_name="Patchfirst", middle_name="Patchmiddle", last_name="Patchlast"))

    new_contacts = db.get_contact_list()

    assert sorted(old_contacts, key=Contact.id_or_max) != sorted(
        new_contacts, key=Contact.id_or_max)

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contact_list(), key=Contact.id_or_max)
