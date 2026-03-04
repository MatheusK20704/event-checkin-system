import re
from src.models import Attendee


class RegistrationService:
    def __init__(self, repo):
        self.repo = repo

    def register(self, event_id, name, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email")

        attendees = self.repo.get_by_event(event_id)
        if any(a.email == email for a in attendees):
            raise ValueError("Duplicate email")

        attendee = Attendee(name, email)
        self.repo.add(event_id, attendee)


class CheckInService:
    def __init__(self, repo):
        self.repo = repo

    def check_in(self, event_id, email):
        attendees = self.repo.get_by_event(event_id)

        for attendee in attendees:
            if attendee.email == email:
                if attendee.checked_in:
                    raise ValueError("Already checked in")
                attendee.checked_in = True
                self.repo.update(event_id, attendee)
                return

        raise ValueError("Not registered")


class ReportService:
    def __init__(self, repo):
        self.repo = repo

    def generate(self, event_id):
        attendees = self.repo.get_by_event(event_id)
        total_registered = len(attendees)
        checked_in = [a.name for a in attendees if a.checked_in]

        return {
            "total_registered": total_registered,
            "total_checked_in": len(checked_in),
            "checked_in_list": checked_in,
        }