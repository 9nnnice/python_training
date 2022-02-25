import random
import time

from fixture.group import Group
from fixture.contact import Contact
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_add_contacts_to_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    # Выбираем группу
    groups = app.orm.get_group_list()
    group = random.choice(groups)

    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))

    # Выбираем контакты не в группе
    contacts = app.orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)

    # Добавляем контакт в группу
    app.contact.add_to_group(contact, group)

    # Фильтруем по группе контакты, получаем список контактов и сравниваем из бд
    ui_contacts = app.contact.get_group_contact_list(group)
    db_contacts = app.orm.get_contacts_in_group(group)
    assert sorted(ui_contacts, key=Contact.id_or_max) == sorted(db_contacts, key=Contact.id_or_max)


def test_remove_contact_from_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    app.open_home_page()

    # Выбираем группу
    groups = app.orm.get_group_list()
    group = random.choice(groups)

    # Фильтруем контакты по группе
    Select(app.wd.find_element(By.NAME, 'group')).select_by_value(group.id)

    # Выбираем контакты из группы
    contacts = app.orm.get_contacts_in_group(group)

    # Если в группе нет контактов, то добавляем новый и снова получаем список
    if len(contacts) == 0:
        app.contact.create(Contact(first_name='Awesome', last_name='Contact'), group)
        time.sleep(1)
        contacts = app.orm.get_contacts_in_group(group)

    contact = random.choice(contacts)

    # Удаляем контакт из группы
    app.contact.remove_from_group(contact, group)

    # Фильтруем по группе контакты, получаем список контактов и сравниваем из бд
    ui_contacts = app.contact.get_group_contact_list(group)
    db_contacts = app.orm.get_contacts_in_group(group)
    assert sorted(ui_contacts, key=Contact.id_or_max) == sorted(db_contacts, key=Contact.id_or_max)

