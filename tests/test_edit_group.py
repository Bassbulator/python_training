from model.group import Group


def edit_first_group(app):
    app.open_homepage()
    app.group.edit_first_group(Group(name="New group"))
    app.group.return_to_groups_page()
