import pytest

import tasks


@pytest.mark.parametrize('arr1,arr2,result', [
    ([], [], []),
    ([1, 2], [], []),
    ([], [3, 4], []),
    ([1, 2], [3, 4], [(1, 3), (2, 4)]),
    ([1, 2, 5, 6], [3, 4], [(1, 3), (2, 4)]),
])
def test_pairs(arr1, arr2, result):
    assert tasks.corresponding_pairs(arr1, arr2) == result
