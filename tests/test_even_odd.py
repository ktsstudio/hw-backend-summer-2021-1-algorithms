import pytest

import tasks


@pytest.mark.parametrize(
    "arr,res",
    [
        ([], 0),
        ([1, 1, 1, 1], 0),
        ([2, 2, 2, 2], 0),
        ([0, 0, 0, 0], 0),
        ([0], 0),
        ([1, -1], 0),
        ([2, -2, 4], 0),
        ([2, -2, 5], 0),
        ([2, -1, 3], 1),
    ],
)
def test_even_odd(arr: list[int], res: float) -> None:
    assert tasks.even_odd(arr) == res
