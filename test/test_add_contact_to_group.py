import random
from time import sleep
from fixture.orm import ORMFixture
from fixture.contact import Contact
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement


def test_add_contacts_to_group(app):
    # Выбираем группу
    groups = app.orm.get_group_list()
    group = random.choice(groups)

    # Выбираем контакты
    contacts = app.orm.get_contacts_not_in_group(group)

    # Добавляем контакты в группу
    for contact in contacts:
        app.contact.add_to_group(contact, group)

    # Фильтруем по группе контакты, получаем список контактов и сравниваем из бд
    ui_contacts = app.contact.get_group_contact_list(group)
    db_contacts = app.orm.get_contacts_in_group(group)
    assert sorted(ui_contacts, key=Contact.id_or_max) == sorted(db_contacts, key=Contact.id_or_max)


def test_remove_contact_from_group(app):
    # Выбираем группу
    groups = app.orm.get_group_list()
    group = random.choice(groups)

    # Фильтруем контакты по группе
    Select(app.wd.find_element(By.NAME, 'group')).select_by_value(group.id)

    # Выбираем контакт
    contacts = app.orm.get_contacts_in_group(group)
    contact = random.choice(contacts)

    # Удаляем контакт из группы
    app.contact.remove_from_group(contact, group)

    # Фильтруем по группе контакты, получаем список контактов и сравниваем из бд
    ui_contacts = app.contact.get_group_contact_list(group)
    db_contacts = app.orm.get_contacts_in_group(group)
    assert sorted(ui_contacts, key=Contact.id_or_max) == sorted(db_contacts, key=Contact.id_or_max)

