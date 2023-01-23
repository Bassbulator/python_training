# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.add_new_contact(Contact(firstname="Maksim", middlename="Andreevich", lastname="Belikov",
                                        nickname="Bassbulator", company="qwerty", address="qwerty", mobile="12345678",
                                        email="qwerty@mail.ru"))

