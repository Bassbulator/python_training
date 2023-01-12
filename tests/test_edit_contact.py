from model.contact import Contact


def test_edit_first_contact(app):
    app.open_homepage()
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Maksim1", middlename="Andreevich1", lastname="Belikov1", nickname="Bassbulator", company="qwerty", address="qwerty", mobile="12345678", email="qwerty@mail.ru"))
    app.contact.return_homepage()
    app.session.logout()