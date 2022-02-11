from model.contact import Contact
from random import randrange

def test_modify_contact(app, db):
    if app.contact.count() == 0:
        db.create(Contact(first_name="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="Patchfirst", middle_name="Patchmiddle", last_name="Patchlast")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(contact, index)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)