from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(nickname="Patch nickname", title="Patch title", company="Patch title"))
    app.session.logout()