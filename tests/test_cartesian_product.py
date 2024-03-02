import pytest

import tasks


@pytest.mark.parametrize(
    "arr1,arr2,result",
    [
        ([], [], []),
        ([1, 2], [], []),
        ([], [3, 4], []),
        ([1, 2], [3, 4], [(1, 3), (1, 4), (2, 3), (2, 4)]),
        (
            [1, 2, 5, 6],
            [3, 4],
            [(1, 3), (1, 4), (2, 3), (2, 4), (5, 3), (5, 4), (6, 3), (6, 4)],
        ),
    ],
)
def test_cartesian_product(arr1: list, arr2: list, result: list[tuple]) -> None:
    assert tasks.cartesian_product(arr1, arr2) == result
