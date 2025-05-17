from collections import UserDict
from pprint import pprint


class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass
    # def __init__(self, value):
    #     # Logic
    #     super().__init__(value)

class Phone(Field):
    def __init__(self, value: str):
        if len(value) != 10 or not value.isdigit():
            raise ValueError

        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_str: str):
        phone = Phone(phone_str)
        self.phones.append(phone)

    def find_phone(self, phone_str: str):
        for i in self.phones:
            if i.value == phone_str:
                return i

        return None

    def remove_phone(self, phone: str):
        # self.phones = [p for p in self.phones if p.value != phone]
        self.phones.remove (self.find_phone(phone))


    def edit_phone(self, current_phone, new_phone):
        if self.find_phone(current_phone) is None:
            raise ValueError

        # Validation
        Phone(new_phone)

        self.remove_phone(current_phone)
        self.add_phone(new_phone)



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

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
