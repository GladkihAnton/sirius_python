Дан массив целочисленных значений nums, отсортированный в неубывающем порядке, удалите дубликаты на месте так, чтобы каждый уникальный элемент появлялся только один раз. Порядок элементов должен оставаться тем же. Верните количество уникальных элементов в nums.

Предположим, что k - это количество уникальных элементов в nums. Чтобы решение прошло все тесты, нужно выполнить следующие действия:

Изменить массив nums так, чтобы первые k элементов nums содержали уникальные элементы в том же порядке, в каком они были изначально в массиве nums.
Вернуть значение k.
Тестирующая система:


Пример 1:
```
Ввод: nums = [1,1,2]
Вывод: 2, nums = [1,2,_]
Пояснение: Ваша функция должна вернуть k = 2, причем первые два элементы в nums это 1 и 2, в том же порядке, что и в изначальном nums.
Не имеет значения, что будет идти после k элементов (для примера они равны нижнему подчеркиванию).
```
Пример 2:
```
Ввод: nums = [0,0,1,1,1,2,2,3,3,4]
Вывод: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Пояснение: Ваша функция должна вернуть k = 5, причем первые два элементы в nums это 0, 1, 2, 3 и 4, в том же порядке, что и в изначальном nums.
Не имеет значения, что будет идти после k элементов (для примера они равны нижнему подчеркиванию).
```