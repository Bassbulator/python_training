from model.contact import Contact
import random


def test_delete_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(Contact(firstname="Maksim", middlename="Andreevich", lastname="Belikov",
                                            homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
