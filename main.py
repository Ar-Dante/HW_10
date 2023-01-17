from collections import UserDict
from datetime import datetime
import re


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value.isdigit():
            self.__value = new_value
        else:
            print('Номер має містити тільки цифри!')


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        regex = re.compile("[0-9]{2}\-[0-9]{2}\-[0-9]{4}")
        match = re.match(regex, new_value)
        if match:
            self.__value = new_value
        else:
            print("Неправильний формат даних, має бути ДД-ММ-РРРР")

class Record(Field):
    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.bd = Birthday(birthday)
        if phone:
            self.phone = [Phone(phone)]
        else:
            self.phone = []
    def days_to_birthday(self):
        d1 = datetime.today()
        d2 = datetime.strptime(self.bd.value, "%d-%m-%Y")
        delta1 = datetime(d1.year, d2.month, d2.day)
        delta2 = datetime(d1.year + 1, d2.month, d2.day)
        return f'До дня народження залишолсь {((delta1 if delta1 > d1 else delta2) - d1).days} днів'

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

    def print_n_item(self, N=2):
        page = 1
        counter = 0
        result = "Address Book:"
        for i, j in self.data.items():
            result += f'\n{i}: {j}'
            counter += 1
            if counter >= N:
                yield result
                result = f'\nPage: {page}\n'
                counter = 0
                page += 1

        yield result

    def iterator(self, n):
        gen = self.print_n_item(n)
        result = ""
        for i in gen:
            result += i
            print(result)
            result = ""
            next = input(f'Press any key for next: ')
            if next:
                continue


if __name__ == '__main__':
    name = 'Bill'
    phone = '1234567890'
    birthday = '01-05-2003'
    rec = Record(name, phone, birthday)
    print(rec.days_to_birthday())
    ab = AddressBook()
    rec1 = Record("A", '1312312', '01-02-3423')
    rec2 = Record("B", '1213312312', '11-02-3423')
    rec3 = Record("C", '131231312', '12-02-3423')
    rec4 = Record("D", '131232312', '13-02-1423')
    rec5 = Record("E", '1312312312', '14-02-3423')
    rec6 = Record("F", '1312311232', '15-02-3423')
    ab.add_record(rec)
    ab.add_record(rec1)
    ab.add_record(rec2)
    ab.add_record(rec3)
    ab.add_record(rec4)
    ab.add_record(rec5)
    ab.add_record(rec6)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phone, list)
    assert isinstance(ab['Bill'].phone[0], Phone)
    assert ab['Bill'].phone[0].value == '1234567890'
    print(ab.data)

    print('Test DONE!')