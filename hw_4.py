from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def get_name(self):
        return self.value

    def set_name(self, name):
        self.value = name

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Invalid phone number format")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.get_name() != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.get_name() == old_phone:
                phone.set_name(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.get_name() == phone:
                return p.get_name()

    def __str__(self):
        phones = "; ".join([str(p) for p in self.phones])
        return f"Contact name: {self.name.get_name()}, phones: {phones}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.get_name()] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    found_phone = john.find_phone("5555555555")
    print(f"{john.name.get_name()}: {found_phone}")  # Виведення: 5555555555

    book.delete("Jane")