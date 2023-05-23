from model.contact import Contact
import random
from random import randrange


def test_edit_contact_firstname(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(firstname="Maksim", middlename="Andreevich", lastname="Belikov",
                                            homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None))
    new_contact_data = Contact(firstname="New firstname", middlename="New middlename", lastname="New lastname")
    old_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    index = randrange(len(old_contacts))
    new_contact_data.id = old_contacts[index].id
    app.contact.edit_contact_by_id(new_contact_data.id, new_contact_data)
    mod_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(old_contacts) == len(mod_contacts)
    old_contacts[index] = new_contact_data
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(mod_contacts, key=Contact.id_or_max)
    if check_ui:
        assert (sorted(mod_contacts, key=Contact.id_or_max) ==
                sorted(app.contact.get_contact_list(), key=Contact.id_or_max))
