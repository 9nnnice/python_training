# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Test", middle_name="Testov", last_name="Testovich", nickname="patch", company="companypatch", title="titlepatch"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="", middle_name="", last_name=""))
    app.session.logout()
