first = int(input())
second = int(input())

number = 0
while True:
    number += 1
    if number % first == 0 and number % second == 0:
        print(number)
        break
