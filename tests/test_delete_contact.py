from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(firstname="Maksim", middlename="Andreevich", lastname="Belikov", nickname="Bassbulator",
                                            company="qwerty", address="qwerty", mobile="12345678", email="qwerty@mail.ru"))
    app.contact.delete_first_contact()
    