import re
import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(
            host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(
                    Group(id=str(id), name=re.sub(' +', ' ', name).strip()))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(
                    Contact(id=str(id), first_name=firstname, last_name=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_by_id(self, id):
        list = []
        cursor = self.connection.cursor()
        try:
            query = "select id, firstname, lastname, address, home, mobile, work, fax, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00' and id=%s" % id
            cursor.execute(query)
            for row in cursor:
                (id, firstname, lastname, address, home,
                 mobile, work, fax, email, email2, email3) = row
                list.append(Contact(id=str(id), first_name=firstname,
                            last_name=lastname, address=address, homephone=home,
                            mobilephone=mobile, workphone=work, secondhomephone=fax,
                            email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list[0]

    def destroy(self):
        self.connection.close()
