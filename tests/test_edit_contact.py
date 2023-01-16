from model.contact import ModifyContact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(ModifyContact(new_firstname="Maksim1", new_middlename="Andreevich1", new_lastname="Belikov1",
                                           new_nickname="Bassbulator", new_company="qwerty", new_address="qwerty",
                                           new_mobile="12345678", new_email="qwerty@mail.ru"))
    app.contact.return_homepage()