Ввод: haystack = "sadbutsad", needle = "sad"
Вывод: 0
Пояснение: Строка needle = "sad" входит в строку haystack = "sadbutsad" дважды - в индексах 0 и 6.
Первое вхождение в индексе 0, поэтому возвращаем 0.
Ограничения: Нельзя использовать .index(). Задача в том и состоит, чтобы его написать

Пример 1:
```
Ввод: haystack = "sadbutsad", needle = "sad"
Вывод: 0
Пояснение: Строка needle = "sad" входит в строку haystack = "sadbutsad" дважды - в индексах 0 и 6.
Первое вхождение в индексе 0, поэтому возвращаем 0.
```

Пример 2:
```
Ввод: haystack = "leetcode", needle = "leeto"
Вывод: -1
Пояснение: "leeto" не входит в строку "leetcode", поэтому возвращаем -1.
```
 