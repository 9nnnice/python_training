from model.contact import Contact
from random import randrange
import re


def test_alldata_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()

    for ui_contact in contacts_from_home_page:
        db_contact = db.get_contact_by_id(ui_contact.id)
        assert ui_contact.first_name == db_contact.first_name
        assert ui_contact.last_name == db_contact.last_name
        assert ui_contact.address == db_contact.address
        assert ui_contact.all_phones_from_home_page == merge_phones_like_on_home_page(
            db_contact)
        assert ui_contact.all_emails_from_home_page == merge_emails_like_on_home_page(
            db_contact)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondhomephone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
