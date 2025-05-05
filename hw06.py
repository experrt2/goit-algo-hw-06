from collections import UserDict
from pprint import pprint


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass
    # def __init__(self, value):
    #     # Logic
    #     super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError

        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_str: str):
        phone = Phone(phone_str)
        self.phones.append(phone)

    def remove_phone(self, phone: str):
        # phones  = [Phone(), Phone(), Phone()]
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, current_phone, new_phone):
        self.remove_phone(current_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone_str: str):
        for i in self.phones:
            if i.value == phone_str:
                return i

        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        return self.data.pop(name)

    def __str__(self):
        result = ""
        for key, record in self.data.items():
            result += str(record) + '\n'

        return result
