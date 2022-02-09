from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contact_list() #заменяй на get_group_list в случае, если нужны группы
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()