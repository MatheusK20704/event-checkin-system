from dataclasses import dataclass

@dataclass
class Event:
    id: int
    name: str
    date: str

@dataclass
class Attendee:
    name: str
    email: str
    checked_in: bool = False