import re
from random import randrange
from model.contact import Contact

def test_alldata_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)
    # assert contacts_from_home_page.last_name == contacts_from_db.last_name
    # assert contacts_from_home_page.address == contacts_from_db.address
    # assert contacts_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db)
    # assert contacts_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone


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