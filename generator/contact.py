from model.contact import Contact
import random
import string
import os.path
import json


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(first_name="", middle_name="", last_name="")] + [
    Contact(first_name=random_string("Kostyan", 10), middle_name=random_string("Testin", 20), last_name=random_string("Testovich", 20))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contacts.json")

with open(file, "w") as f:
    f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))