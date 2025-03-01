numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# включать числа из nubmers_1 и не включать из numbers_2

# o(n^2)
numbers_3 = []
for number_1 in numbers_1:  # o(n)
    if number_1 in numbers_2:  # o(n) -> o(1)
        continue

    numbers_3.append(number_1)
print(numbers_3)


# o(n^2)
numbers_4 = numbers_1.copy()  # o(n)
for number_4 in numbers_4:
    if number_4 in numbers_2:  # o(n)
        continue

    numbers_3.remove(number_4)  # o(n)


# o(n)
numbers_5 = []
numbers_2 = set(numbers_2)
for number_1 in numbers_1:  # o(n)
    if number_1 in numbers_2:  # o(1)
        continue

    numbers_5.append(number_1)
print(numbers_5)
