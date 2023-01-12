from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):

    pass


class Record(Field):
    def __init__(self, name, phone=None):
        self.name = Name(name)
        if phone:
            self.phone = [Phone(phone)]
        else:
            self.phone = []

    def add_phone(self, ph):
        self.phone.append(ph)

    def change_phone(self, ph, new_ph):
        for i in len(self.phone):
            if self.phone[i] == ph:
                self.phone[i] = new_ph

    def del_phone(self, ph):
        self.phone.remove(ph)


class AddressBook(UserDict):
    def add_record(self, rec):
        self.data[rec.name.value] = rec


if __name__ == '__main__':
    name = 'Bill'
    phone = '1234567890'
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phone, list)
    assert isinstance(ab['Bill'].phone[0], Phone)
    assert ab['Bill'].phone[0].value == '1234567890'
    print('Test DONE!')