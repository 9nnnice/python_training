from model.contact import Contact


def test_modification_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modification(Contact(nickname="Patch nickname", title="Patch title", company="Patch title"))
    app.session.logout()