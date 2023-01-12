from model.group import Group


def edit_first_group(app):
    app.open_homepage()
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="New group"))
    app.group.return_to_groups_page()
    app.session.logout()
