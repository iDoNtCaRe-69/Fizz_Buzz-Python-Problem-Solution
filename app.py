def fizz_buzz(input):
    if input % 15 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Buzz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(input_your_number))
