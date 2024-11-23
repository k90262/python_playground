from src.fizzbuss import fizzbuss, print_fizzbuzz

def test_fizzbuss_normal_number():
    assert fizzbuss(1) == "1"
    assert fizzbuss(2) == "2"

def test_fizzbuss_three_is_fizz():
    assert fizzbuss(3) == "Fizz"

def test_fizzbuss_five_is_buzz():
    assert fizzbuss(5) == "Buzz"

def test_fizzbuss_fifteen_is_fizzbuzz():
    assert fizzbuss(15) == "FizzBuzz"

def test_print_fizzbuss(capsys):
    print_fizzbuzz(3)
    captured_stdout = capsys.readouterr().out
    assert captured_stdout == "1\n2\nFizz\n"