# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="qwerty", header="qwerty", footer="qwerty"))
    app.group.return_to_groups_page()


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_groups_page()

