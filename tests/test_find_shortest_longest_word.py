import pytest

import tasks


@pytest.mark.parametrize(
    "text,words",
    [
        ("", (None, None)),
        ("        ", (None, None)),
        ("\n\n\t", (None, None)),
        ("hello\n\n\tsir", ("sir", "hello")),
        ("hello there, general kenobi", ("hello", "general")),
        ("привет всем", ("всем", "привет")),
        ("привет", ("привет", "привет")),
        ("привет       всем", ("всем", "привет")),
    ],
)
def test_find_shortest_longest_word(
    text: str, words: tuple[str, str] | tuple[None, None]
) -> None:
    assert tasks.find_shortest_longest_word(text) == words
