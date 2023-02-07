from model.contact import Contact


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(firstname="Maksim", middlename="Andreevich", lastname="Belikov", nickname="Bassbulator",
                                            company="qwerty", address="qwerty", mobile="12345678", email="qwerty@mail.ru"))
    contact = Contact(firstname="New name")
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    mod_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(mod_contacts, key=Contact.id_or_max)

def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(
            Contact(firstname="Maksim", middlename="Andreevich", lastname="Belikov", nickname="Bassbulator",
                    company="qwerty", address="qwerty", mobile="12345678", email="qwerty@mail.ru"))
    contact = Contact(lastname="New name")
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    mod_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(mod_contacts, key=Contact.id_or_max)


def test_edit_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(
            Contact(firstname="Maksim", middlename="Andreevich", lastname="Belikov", nickname="Bassbulator",
                    company="qwerty", address="qwerty", mobile="12345678", email="qwerty@mail.ru"))
    contact = Contact(middlename="New name")
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    mod_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(mod_contacts, key=Contact.id_or_max)