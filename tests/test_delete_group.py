def test_delete_first_group(app):
    app.open_homepage()
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.group.return_to_groups_page()
    app.session.logout()