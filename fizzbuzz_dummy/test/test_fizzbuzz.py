import pytest

from fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    "number,expected", [
        (2, "2"),
        (3, "Fizz"),
        (5, "Buzz"),
        (15, "FizzBuzz"),
    ]
)
def test_fizzbuzz(number, expected):
    assert fizzbuzz(number, None) == expected
