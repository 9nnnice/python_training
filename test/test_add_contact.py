# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, check_ui, json_contacts):
    contact = json_contacts

    old_contacts = db.get_contact_list()
    old_contacts.append(contact)

    app.contact.create(contact)

    new_contacts = db.get_contact_list()

    assert len(old_contacts) + 1 == len(new_contacts)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)

    if check_ui:
        sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(
            new_contacts, key=Contact.id_or_max)
