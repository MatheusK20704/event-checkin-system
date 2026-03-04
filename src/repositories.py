import json
import os


class FileAttendeeRepository:
    def __init__(self, file_path):
        self.file_path = file_path

        
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def _load(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f)

    def add(self, attendee):
        data = self._load()
        data.append(attendee)
        self._save(data)

    def get_all(self):
        return self._load()

    def find_by_email(self, email):
        data = self._load()
        for attendee in data:
            if attendee.get("email") == email:
                return attendee
        return None

    def update(self, email, updated_attendee):
        data = self._load()
        for i, attendee in enumerate(data):
            if attendee.get("email") == email:
                data[i] = updated_attendee
                self._save(data)
                return