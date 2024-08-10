from typing import List, Optional, Dict
from collections import UserDict
from datetime import datetime, timedelta, date

from .record import Record

WEEK = 7
WORKING_DAYS = 5


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self) -> List[Dict[str, date]]:
        today = datetime.today().date()
        event_from = today
        event_to = today + timedelta(days=WEEK)

        result: List[Dict[str, date]] = []

        for contact in self.data.values():
            b_day = datetime.strptime(contact.birthday.value, "%d.%m.%Y").date()
            b_day = b_day.replace(year=today.year)
            if b_day < event_from or b_day > event_to:
                continue
            if b_day.isoweekday() > WORKING_DAYS:
                correct_to_monday = 1 if b_day.isoweekday() - WORKING_DAYS == 2 else 2
                b_day = b_day + timedelta(days=correct_to_monday)
            result.append({"name": contact.name, "congratulation_date": b_day})

        return result
