from model.group import Group

def test_modification_group(app):
    app.group.modification(Group(name="First name", header="Second name", footer="Public group"))

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))