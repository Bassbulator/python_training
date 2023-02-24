from model.contact import Contact
from random import randrange


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(firstname="Maksim", middlename="Andreevich", lastname="Belikov",
                                            homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None))
    contact = Contact(firstname="New firstname", middlename="New middlename", lastname="New lastname")
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    mod_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(mod_contacts, key=Contact.id_or_max)
