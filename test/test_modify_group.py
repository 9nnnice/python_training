from model.group import Group

def test_modification_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification(Group(name="First name", header="Second name", footer="Public group"))
    app.session.logout()