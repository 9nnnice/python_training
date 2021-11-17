# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(first_name="Kostyan", middle_name="Testin", last_name="Testovich"))


def test_add_empty_contact(app):
    app.contact.create(Contact(first_name="", middle_name="", last_name=""))