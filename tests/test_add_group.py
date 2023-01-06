# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.close)
    return fixture

def test_add_group(app):
    app.open_homepage()
    app.session.login(username="admin", password="secret")
    app.open_groups_page()
    app.init_group_creation()
    app.fill_group_form(Group(name="qwerty", header="qwerty", footer="qwerty"))
    app.submit_group_creation()
    app.return_to_groups_page()
    app.session.logout()


def test_add_empty_group(app):
    app.open_homepage()
    app.session.login(username="admin", password="secret")
    app.open_groups_page()
    app.init_group_creation()
    app.fill_group_form(Group(name="", header="", footer=""))
    app.submit_group_creation()
    app.return_to_groups_page()
    app.session.logout()

