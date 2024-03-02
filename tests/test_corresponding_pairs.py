from typing import Any

import pytest

import tasks


@pytest.mark.parametrize(
    "arr1,arr2,result",
    [
        ([], [], []),
        ([1, 2], [], []),
        ([], [3, 4], []),
        ([1, 2], [3, 4], [(1, 3), (2, 4)]),
        ([1, 2, 5, 6], [3, 4], [(1, 3), (2, 4)]),
    ],
)
def test_corresponding_pairs(arr1: list, arr2: list, result: list[tuple[Any, Any]]):
    assert tasks.corresponding_pairs(arr1, arr2) == result
