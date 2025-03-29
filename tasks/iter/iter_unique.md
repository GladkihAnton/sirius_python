Напишите итератор UniqueIterator, который принимает последовательность и возвращает только уникальные элементы в порядке появления.


```python
class OrderedUniqueIterator:
    ...

nums = [1, 2, 2, 3, 4, 4, 5]
unique = OrderedUniqueIterator(nums)
for num in unique:
    print(num)
```