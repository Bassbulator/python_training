# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts):
    added_contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.add_new_contact(added_contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(added_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
