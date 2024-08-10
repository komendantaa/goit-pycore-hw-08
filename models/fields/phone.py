from .field import Field
from ..error import PhoneInvalid


class Phone(Field):
    def __init__(self, value: str):
        self.__validate(value)
        super().__init__(value)

    def update(self, phone: str) -> None:
        self.__validate(phone)
        self.value = phone

    def __validate(self, phone: str) -> None:
        if not phone.isdigit() or len(phone) != 10:
            raise PhoneInvalid(f"Invalid phone number: {phone}")
