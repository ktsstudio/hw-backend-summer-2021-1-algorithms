import pytest

import tasks


@pytest.mark.parametrize(
    "seconds,result",
    [
        (0, "00s"),
        (1, "01s"),
        (5, "05s"),
        (10, "10s"),
        (60, "01m00s"),
        (75, "01m15s"),
        (3700, "01h01m40s"),
        (93600, "01d02h00m00s"),
        (864000, "10d00h00m00s"),
    ],
)
def test_seconds_to_str(seconds: int, result: str):
    assert tasks.seconds_to_str(seconds) == result
