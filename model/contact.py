from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None,
                 mobile=None, email=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.mobile = mobile
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.middlename)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) \
               and self.firstname == other.firstname or self.firstname is None or other.firstname is None\
               and self.lastname == other.lastname or self.lastname is None or other.lastname is None \
               and self.middlename == other.middlename or self.middlename is None or other.middlename is None

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
