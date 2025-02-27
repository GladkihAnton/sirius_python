from collections import deque

# array
list_ = [1, 2, 3, 4, 5, 6, 7]  # len() = 6, cap() = 12
list_ = [1, 2, 3, 4, 99, 5, 6, 7]  # len() = 6, cap() = 12
print(5 in list_)


list_.remove(1)  # (o(1))
list_.insert(3, 5)

# linked list
deque_ = deque()

# deque_.append()  # o(1)
# deque_.appendleft()  # o(1)
# 5 in deque  # o(n)

# print(deque_[3])  # o(n)
# print(deque_.remove(3))  # o(n)
# del deque_[3]  # o(n)

tuple_ = tuple()
list_big = [None] * 100
list_big[0] = 1
list_big[1] = 2
list_big[3] = 3
...

set_ = set()
dict_ = dict()

print(hash('asdas'))  # hash() -> hash
print(hash('asdas'))  # hash() -> hash
# Hashable
print(5 in dict_)  # o(n) -> максимльная глубина коллизии
print(dict_[5])  # o(n) -> максимльная глубина коллизии
dict_[5] = 2  # o(1)
del dict_[5]  # o(n) -> максимльная глубина коллизии
