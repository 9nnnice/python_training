from model.contact import Contact
import random
import string

constant = [
    Contact(first_name="Kostyan", middle_name="Testin", last_name="Testovich"),
    Contact(first_name="Kostyan2", middle_name="Testin2", last_name="Testovich2"),
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(first_name="", middle_name="", last_name="")] + [
    Contact(first_name=random_string("Kostyan", 10), middle_name=random_string("Testin", 20), last_name=random_string("Testovich", 20))
    for i in range(5)
]