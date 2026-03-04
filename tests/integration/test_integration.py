from src.repositories import FileAttendeeRepository
from src.services import RegistrationService, CheckInService, ReportService


def test_persistence(tmp_path):
    file_path = tmp_path / "data.json"

    repo = FileAttendeeRepository(file_path)
    reg = RegistrationService(repo)

    reg.register(1, "John", "john@email.com")

    repo2 = FileAttendeeRepository(file_path)
    attendees = repo2.get_by_event(1)

    assert len(attendees) == 1


def test_register_and_checkin_flow(tmp_path):
    file_path = tmp_path / "data.json"

    repo = FileAttendeeRepository(file_path)
    reg = RegistrationService(repo)
    check = CheckInService(repo)
    report = ReportService(repo)

    reg.register(1, "A", "a@email.com")
    reg.register(1, "B", "b@email.com")
    check.check_in(1, "a@email.com")

    result = report.generate(1)

    assert result["total_registered"] == 2
    assert result["total_checked_in"] == 1


def test_full_workflow(tmp_path):
    file_path = tmp_path / "data.json"

    repo = FileAttendeeRepository(file_path)
    reg = RegistrationService(repo)
    check = CheckInService(repo)
    report = ReportService(repo)

    reg.register(99, "User", "user@email.com")
    check.check_in(99, "user@email.com")

    result = report.generate(99)

    assert result["total_checked_in"] == 1