# iterable full memory __iter__ -> iterator
# iterator - __next__

# generator = dynamic memory


a = [1, 2, 3]
print(type(iter(a)))
# 1) создать итератор
# 2) использовать нехт у итератора
items = [1, 2, 3]
for item in items:  # try: next(next(iter(items))) except StopIteration: ...
    ...

iter_items = iter(items)
print(next(iter_items))
print(next(iter_items))
print(next(iter_items))  # next next() -> StopIteration

print('example')
iter_items_example = iter(items)
while True:
    try:
        print(next(iter_items_example))
    except StopIteration:
        break


class MyList:
    def __init__(self, *args):
        self.array = [*args]
        self.last_element = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        result = self.array[self.last_element]
        self.last_element += 1
        return result


def gen_list(stop: int):
    step = 0
    while True:
        print(step)
        step = step + 1
        if step == stop:
            return

        yield step

# for item in MyList(1, 2, 3, 4, 5):
#     print(item)

for item in gen_list(10):
    print(item)

# list_ = MyList(1, 2, 3, 4, 5)
# print(next(list_))
# print(next(list_))
