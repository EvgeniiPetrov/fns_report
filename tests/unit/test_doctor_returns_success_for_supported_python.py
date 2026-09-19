import fns_reports.cli


def test_doctor_returns_success_for_supported_python():
    result: str | None = fns_reports.cli.main()
    expected: str = "main"
    assert result is expected
