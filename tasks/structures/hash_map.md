Реализовать "свой" дикт.
Для простоты ключ должен быть строкой, значение числом
Разрешается использовать сам дикт, но нельзя "использовать" его внутренний хэш. Следует использовать

Подсказка: В решение рекомендую использовать list + tuple
```python
storage = {}

hash_func = len
def put(key: str, value: int) -> None: # o(1)
    # usage example
    hash_ = hash_func('string')
    ...

def get(key: str) -> int: # o(n), где n - глубина коллизии ключа key. Иными словами, максимальное количество элементов с одинаковым хэшом
    return ...

```
