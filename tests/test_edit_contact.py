from model.contact import Contact


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(firstname="Maksim", middlename="Andreevich", lastname="Belikov", nickname="Bassbulator",
                                            company="qwerty", address="qwerty", mobile="12345678", email="qwerty@mail.ru"))
    app.contact.edit_first_contact(Contact(firstname="New name"))

def test_edit_contact_lastname(app):
    app.contact.edit_first_contact(Contact(lastname="New lastname"))


def test_edit_contact_middlename(app):
    app.contact.edit_first_contact(Contact(middlename="New middlename"))