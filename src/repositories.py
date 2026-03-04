class FileAttendeeRepository:
    def add(self, event_id, attendee):
        raise NotImplementedError

    def get_by_event(self, event_id):
        raise NotImplementedError

    def update(self, event_id, attendee):
        raise NotImplementedError


class InMemoryAttendeeRepository(FileAttendeeRepository):
    def __init__(self):
        self.storage = {}

    def add(self, event_id, attendee):
        self.storage.setdefault(event_id, []).append(attendee)

    def get_by_event(self, event_id):
        return self.storage.get(event_id, [])

    def update(self, event_id, updated_attendee):
        attendees = self.storage.get(event_id, [])
        for i, a in enumerate(attendees):
            if a.email == updated_attendee.email:
                attendees[i] = updated_attendee
                return