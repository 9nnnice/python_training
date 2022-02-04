

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = db.getgrouplist()
    assert sorted(ui_list) == sorted(db_list)