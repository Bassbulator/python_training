from model.group import Group

def test_add_group(app):
    app.open_homepage()
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="qwerty", header="qwerty", footer="qwerty"))
    app.group.return_to_groups_page()
    app.session.logout()