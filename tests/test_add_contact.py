# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    added_contact = Contact(firstname="Maksim", middlename="Andreevich", lastname="Belikov",
                                        nickname="Bassbulator", company="qwerty", address="qwerty", mobile="12345678",
                                        email="qwerty@mail.ru")
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new_contact(added_contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(added_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)