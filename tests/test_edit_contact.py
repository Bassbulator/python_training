from model.contact import Contact


def test_edit_contact_firstname(app):
    app.contact.edit_first_contact(Contact(firstname="New name"))
    app.contact.return_homepage()

def test_edit_contact_lastname(app):
    app.contact.edit_first_contact(Contact(lastname="New lastname"))
    app.contact.return_homepage()


def test_edit_contact_middlename(app):
    app.contact.edit_first_contact(Contact(middlename="New middlename"))
    app.contact.return_homepage()