"Требуется создать итератор CycleList, который принимает список и бесконечно перебирает его элементы по кругу."
"""
class CycleList:
    ...

cycle = CycleList([1, 2, 3])
for index, num in enumerate(cycle):
    if index == 7:
        break
    print(num)
"""

class CycleList:
    def __init__(self, cycle):
        self.cycle = cycle

    def __iter__(self):
        return CycleListIterator(self.cycle)


class CycleListIterator:

    def __init__(self, cycle):
        self.step = 0
        self.cycle = cycle

    def __next__(self):
        result = self.cycle[self.step % len(self.cycle)]
        self.step += 1
        return result





cycle = CycleList([1, 2, 3])
for index, num in enumerate(cycle):
    if index == 7:
        break
    print(num)
