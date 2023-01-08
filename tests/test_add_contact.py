# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.close)
    return fixture


def test_add_contact(app):
    app.open_homepage()
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact(Contact(firstname="Maksim", middlename="Andreevich", lastname="Belikov", nickname="Bassbulator", company="qwerty", address="qwerty", mobile="12345678", email="qwerty@mail.ru"))
    app.contact.return_homepage()
    app.session.logout()

