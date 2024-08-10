from datetime import datetime

from config import DATE_FORMAT
from .field import Field
from ..error import BirthdayInvalid


class Birthday(Field):
    def __init__(self, value):
        self.__validate(value)
        super().__init__(value)

    def __validate(self, value: str) -> None:
        try:
            datetime.strptime(value, DATE_FORMAT)
        except ValueError:
            raise BirthdayInvalid("Invalid date format. Use DD.MM.YYYY")
