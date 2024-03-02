import pytest

import tasks


@pytest.mark.parametrize(
    "d1,d2",
    [
        (
            {"key1": "value1", "key2": "value2"},
            {
                "value1": "key1",
                "value2": "key2",
            },
        ),
        ({}, {}),
        (
            {"key1": "value1", "key2": "value1"},
            {
                "value1": "key2",
            },
        ),
    ],
)
def test_flip_kv_vk(d1: dict, d2: dict) -> None:
    assert tasks.flip_kv_vk(d1) == d2


@pytest.mark.parametrize(
    "d1,d2",
    [
        (
            {"key1": "value1", "key2": "value2"},
            {
                "value1": ["key1"],
                "value2": ["key2"],
            },
        ),
        ({}, {}),
        (
            {"key1": "value1", "key2": "value1"},
            {
                "value1": ["key1", "key2"],
            },
        ),
    ],
)
def test_flip_kv_vk_safe(d1: dict, d2: dict) -> None:
    assert tasks.flip_kv_vk_safe(d1) == d2
