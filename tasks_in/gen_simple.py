"""Реализуйте генератор prime_generator(), который лениво генерирует простые числа (2, 3, 5, 7, 11, …) без ограничения.


def prime_generator():
    ...


gen = prime_generator()
for _ in range(10):
    print(next(gen))
"""

try:
    ...
except Exception:
    ...
else:
    ...
finally:
    ...

def prime_generator():
    elem = 2
    while True:
        for i in range(2, elem):
            if elem % i == 0:
                print(f'break {elem=}')
                break
        else:
            print(f'else {elem=}')
            yield elem
        elem += 1

gen = prime_generator()
for _ in range(10):
    print(next(gen))

