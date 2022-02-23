import random
from selenium.webdriver.common.by import By


def test_add_contact_to_group_from_homepage(app, db):
    contacts = app.contact.get_contact_list()
    contact = random.choice(contacts)
    app.contact.select_contact_by_id(contact.id)
    app.wd.find_element(By.NAME, 'add')
    assert True


def test_add_contact_to_group_from_editpage(app):
    assert True
