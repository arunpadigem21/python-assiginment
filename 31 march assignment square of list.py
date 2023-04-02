def sum_of_squares():
    numbers = []
    n = int(input("Enter size of  list: "))
    for i in range(n):
        num = int(input("Enter the number: "))
        numbers.append(num)
    sum_of_squares = 0
    for num in numbers:
        sum_of_squares += num ** 2
    return sum_of_squares
print(sum_of_squares())
