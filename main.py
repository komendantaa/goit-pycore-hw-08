import pickle
from typing import List, Dict, cast
from datetime import date

from decorators import input_error, contact_exists
from utils import parse_input
from models import AddressBook, Record, Birthday


@input_error
# @contact_exists(False)
def add_contact(args: List[str], book: AddressBook) -> str:
    name, phone, *_ = args
    record = book.find(name)
    if record:
        record.put_phone(phone)
        return "Contact updated."
    record = Record(name)
    record.put_phone(phone)
    book.add_record(record)
    return "Contact added."


@input_error
@contact_exists()
def change_contact(args: List[str], book: AddressBook) -> str:
    name, curr_phone, new_phone, *_ = args
    record = book.find(name)
    record = cast(Record, record)
    record.edit_phone(curr_phone, new_phone)
    return "Contact changed."


@input_error
@contact_exists()
def show_phone(args: List[str], book: AddressBook) -> Record | None:
    name = args[0]
    return book.find(name)


@input_error
@contact_exists()
def delete_contact(args: List[str], book: AddressBook) -> str:
    name = args[0]
    book.delete(name)
    return "Contact removed."


@input_error
@contact_exists()
def add_birthday(args: List[str], book: AddressBook) -> str:
    name, birthday, *_ = args
    record = book.find(name)
    record = cast(Record, record)
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
@contact_exists()
def show_birthday(args: List[str], book: AddressBook) -> Birthday | None:
    name = args[0]
    record = book.find(name)
    record = cast(Record, record)
    return record.birthday


@input_error
def birthdays(args: List[str], book: AddressBook) -> str:
    return book.get_upcoming_birthdays()


def load_data(filename="addressbook.pkl") -> AddressBook:
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def save_data(book: AddressBook, filename="addressbook.pkl") -> None:
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def main():
    # Завантаження даних з файлу
    book: AddressBook = load_data()
    print("Welcome to the assistant bot!")

    # Цикл введення команд користувача
    while True:
        user_input = input("Enter a command: ")
        cmd, args = parse_input(user_input)

        if cmd in ["close", "exit"]:
            print("Goodbye!")
            break
        elif cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            print(add_contact(args, book))
        elif cmd in ["change", "update"]:
            print(change_contact(args, book))
        elif cmd in ["phone", "show"]:
            print(show_phone(args, book))
        elif cmd in ["delete", "remove"]:
            print(delete_contact(args, book))
        elif cmd == "add-birthday":
            print(add_birthday(args, book))
        elif cmd == "show-birthday":
            print(show_birthday(args, book))
        elif cmd == "birthdays":
            print(birthdays(args, book))
        elif cmd == "all":
            print(book)
        else:
            print("Invalid command.")

    # Збереження даних у файл
    save_data(book)


if __name__ == "__main__":
    main()
