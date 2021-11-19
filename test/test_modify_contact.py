from model.contact import Contact


def test_modification_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    app.contact.modification(Contact(first_name="Patchfirst", middle_name="Patchmiddle", last_name="Patchlast"))