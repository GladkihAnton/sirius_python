Напишите генератор words_from_sentence(sentence), который принимает строку и возвращает слова по одному.

```python
gen = words_from_sentence("Раздели меня пробелами")
for word in gen:
    print(word)
```

(!) Решение не должно использовать split, так как суть генератора тогда теряется