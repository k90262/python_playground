from src.fizzbuss import fizzbuss


# x 1 -> 1
# 2 -> 2
# 3 -> "Fizz"
# 5 -> "Buzz"
# 15 -> "FizzBuzz"
# print up to 100


def test_fizzbuss_one_is_one():
    assert fizzbuss(1) == "1"