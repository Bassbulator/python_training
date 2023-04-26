# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=random_string('firstname', 10),
                    middlename=random_string('middlename', 10),
                    lastname=random_string('lastname', 10),
                    nickname=random_string('nickname', 10),
                    company=random_string('company', 10),
                    address=random_string('address', 10),
                    email=random_string('email', 10),
                    mobilephone=random_string('mobilephone', 10),
                    homephone=random_string('home', 10),
                    secondaryphone=random_string('phone2', 10))]


@pytest.mark.parametrize("added_contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, added_contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new_contact(added_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(added_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)