import pytest

import tasks


@pytest.mark.parametrize(
    "number,flag",
    [
        (1, False),
        (0, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (113, True),
        (199, True),
        (1999, True),
        (2000, False),
    ],
)
def test_is_prime(number: int, flag: bool) -> None:
    assert tasks.is_prime(number) == flag
