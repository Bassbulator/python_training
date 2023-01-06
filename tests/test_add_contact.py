# -*- coding: utf-8 -*-
import pytest
from fixture.application import ApplicationContact
from contact import Contact

@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.close)
    return fixture


def test_add_contact(app):
    app.open_homepage()
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(firstname="Maksim", middlename="Andreevich", lastname="Belikov", nickname="Bassbulator", company="qwerty", address="qwerty", mobile="12345678", email="qwerty@mail.ru"))
    app.return_homepage()
    app.logout()

