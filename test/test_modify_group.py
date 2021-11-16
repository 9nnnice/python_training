from model.group import Group

def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="First name", header="Second name", footer="Public group"))
    app.session.logout()