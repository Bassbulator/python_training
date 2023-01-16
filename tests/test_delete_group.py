def test_delete_first_group(app):
    app.group.delete_first_group()
    app.group.return_to_groups_page()