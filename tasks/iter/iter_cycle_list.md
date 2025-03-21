Требуется создать итератор CycleList, который принимает список и бесконечно перебирает его элементы по кругу.

```python
class CycleList:
    ...

cycle = CycleList([1, 2, 3])
for index, num in enumerate(cycle):
    if index == 7:
        break
    print(num)
```
