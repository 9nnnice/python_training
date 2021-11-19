from model.contact import Contact


def test_modification_contact(app):
    app.contact.modification(Contact(first_name="Patchfirst", middle_name="Patchmiddle", last_name="Patchlast"))