"""
Напишите итератор UniqueIterator, который принимает последовательность и возвращает только уникальные элементы в порядке появления.


python
class OrderedUniqueIterator:
    ...

nums = [1, 2, 2, 3, 4, 4, 5]
unique = OrderedUniqueIterator(nums)
for num in unique:
    print(num)
"""


class OrderedUniqueIterator:
    def __init__(self, nums):
        self.nums = nums
        self.step = -1
        self.unique = set()

    def __iter__(self):
        return self

    def __next__(self):
        self.step += 1
        if self.step >= len(self.nums):
            raise StopIteration
        if self.nums[self.step] in self.unique:
            while True:
                self.step +=1
                if self.step >= len(self.nums):
                    raise StopIteration
                if self.nums[self.step] not in self.unique:
                    return self.nums[self.step]
        else:
            self.unique.add(self.nums[self.step])
            return self.nums[self.step]






nums = [1, 1, 1, 2, 3]
unique = OrderedUniqueIterator(nums)
for num in unique:
    print(num)
