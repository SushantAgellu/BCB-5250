def sum_of_odds(a, b):
    total = 0
    for number in range(a, b + 1):
        if number % 2 == 1:
            total += number
    return total
a, b = map(int, input("Enter two numbers (a b): ").split())
print(sum_of_odds(a, b))