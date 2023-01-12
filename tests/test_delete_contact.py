from model.contact import Contact


def test_delete_first_contact(app):
    app.open_homepage()
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()
    