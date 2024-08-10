from typing import List
from .fields import Name, Phone, Birthday


class Record:
    def __init__(self, name):
        self.name: Name = Name(name)
        self.phones: List[Phone] = []
        self.birthday = None

    def __repr__(self) -> str:
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {self.birthday or '-'}"

    def put_phone(self, phone: str) -> None:
        found = self.find_phone(phone)
        if not found:
            self.phones.append(Phone(phone))

    def edit_phone(self, curr_phone: str, new_phone: str) -> None:
        found = self.find_phone(curr_phone)
        if found:
            found.update(new_phone)

    def find_phone(self, phone: str) -> Phone | None:
        for _phone in self.phones:
            if _phone == phone:
                return _phone
        return None

    def remove_phone(self, phone: str) -> None:
        self.phones = [p for p in self.phones if p.value != phone]

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)
