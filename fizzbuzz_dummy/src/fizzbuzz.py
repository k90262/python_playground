
def fizzbuzz(n, additional_rules):
    """
    Convert a number to it's name in the game FizzBuzz
    """
    answer = ""
    rules = {3: "Fizz", 5: "Buzz"}
    if additional_rules:
        rules.update(additional_rules)
    # Bug: rules should be sorted consistently
    for divisor in rules.keys():
        if n % divisor == 0:
            answer += rules[divisor]
    if not answer:
        answer = str(n)
    return answer
