from typing import List, Optional, Dict
from collections import UserDict
from datetime import datetime, timedelta, date
from config import DATE_FORMAT
from utils import list_to_numerated_rows

from .record import Record

WEEK = 7
WORKING_DAYS = 5


class AddressBook(UserDict):
    def __repr__(self) -> str:
        return list_to_numerated_rows(list(self.data.values()))

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self) -> str:
        today = datetime.today().date()
        event_from = today
        event_to = today + timedelta(days=WEEK)

        result: List[str] = []

        for contact in self.data.values():
            if contact.birthday is None:
                continue
            b_day = datetime.strptime(contact.birthday.value, DATE_FORMAT).date()
            b_day = b_day.replace(year=today.year)
            if b_day < event_from or b_day > event_to:
                continue
            if b_day.isoweekday() > WORKING_DAYS:
                correct_to_monday = 1 if b_day.isoweekday() - WORKING_DAYS == 2 else 2
                b_day = b_day + timedelta(days=correct_to_monday)
            result.append(
                f"name: {contact.name.value}, congratulation_date: {b_day.strftime(DATE_FORMAT)}"
            )

        if not result:
            return "No upcoming birthdays."
        return list_to_numerated_rows(result)
