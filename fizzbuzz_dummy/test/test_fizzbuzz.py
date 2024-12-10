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
    assert fizzbuzz(number) == expected


@pytest.mark.parametrize(
    "number, additional_rules, expected", [
        (7, {7: "Wizz"}, "Wizz"),
        (21, {7: "Wizz"}, "FizzWizz"),
        (2, {2: "Tuzz"}, "Tuzz"),
        (6, {2: "Tuzz"}, "TuzzFizz"),
    ]
)
def test_fizzbuzz_with_wizz_too(number, additional_rules, expected):
    assert fizzbuzz(number, additional_rules) == expected