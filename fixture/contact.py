import time
import re
import random

from model.contact import Contact
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            time.sleep(1)
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.XPATH, "td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                id = cells[0].find_element(
                    By.NAME, "selected[]").get_attribute("value")
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=firstname, last_name=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_group_contact_list(self, group):
        if self.contact_cache is None:
            time.sleep(1)
            wd = self.app.wd
            selector = Select(wd.find_element(By.NAME, 'group'))
            selector.select_by_value(group.id)
            time.sleep(1)
            self.contact_cache = []
            for row in wd.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.XPATH, "td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                id = cells[0].find_element(By.NAME, "selected[]").get_attribute("value")
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=firstname, last_name=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element(
            By.NAME, "firstname").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        last_name = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        secondhomephone = wd.find_element(
            By.NAME, "phone2").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, id=id, address=address,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondhomephone=secondhomephone, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondhomephone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondhomephone=secondhomephone)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def modify_first_contact(self, new_group_data):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.open_home_page()
        # init contact modification
        wd.find_elements(By.XPATH, "//*[@title='Edit']")[index].click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit contact modification
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_edit_page(id)
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit contact modification
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.ID, id).click()

    def select_first_contact(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements(By.XPATH, "//input[@value='Send e-Mail']")) > 0):
            wd.find_element(By.LINK_TEXT, "home").click()

    def open_edit_page(self, id):
        wd = self.app.wd
        url = self.app.base_url + "edit.php?id=" + id
        if not (wd.current_url.endswith(url)):
            wd.get(url)

    def add_to_group(self, contact, group):
        self.select_contact_by_id(contact.id)
        Select(self.app.wd.find_element(By.NAME, 'to_group')).select_by_value(group.id)
        self.app.wd.find_element(By.CSS_SELECTOR, "input[value='Add to']").click()
        self.open_home_page()

    def remove_from_group(self, contact, group):
        Select(self.app.wd.find_element(By.NAME, 'group')).select_by_value(group.id)
        self.select_contact_by_id(contact.id)
        self.app.wd.find_element(By.NAME, "remove").click()
        self.open_home_page()
