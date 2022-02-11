from model.contact import Contact
from random import randrange
from time import sleep
def test_delete_some_contact(app, db):
    if app.contact.count() == 0:
        db.create(Contact(first_name="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    sleep(1)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.pop(index)
    # old_contacts[index:index+1] = []
    # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)