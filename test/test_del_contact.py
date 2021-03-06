from model.contact import Contact
from time import sleep
import random


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        db.create(Contact(first_name="test"))

    old_contacts = db.get_contact_list()

    contact = random.choice(old_contacts)

    app.contact.delete_contact_by_id(contact.id)

    sleep(1)  # Ждем пока из удалится запись?

    new_contacts = db.get_contact_list()

    assert len(old_contacts) - 1 == len(new_contacts)

    old_contacts.remove(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)

    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(
            new_contacts, key=Contact.id_or_max)
