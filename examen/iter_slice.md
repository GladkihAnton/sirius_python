Создайте итератор Slice, который ведет себя как list[start:stop:step], но не создает новый список, а просто перебирает элементы оригинального списка по нужным индексам.

```python
class Slice:
    ...

data = [10, 20, 30, 40, 50, 60, 70, 80]
smart = Slice(data, start=1, stop=6, step=2)
for item in smart:
    print(item)
```

(!) Не использовать list[start:stop:step] напрямую — итератор должен работать эффективно, без создания копий списка