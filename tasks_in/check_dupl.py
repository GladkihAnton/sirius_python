'''
Дан целочисленный массив nums, верните true, если любое из значений встречается в массиве как минимум дважды, иначе верните false, если все значения в массиве различны.



Пример 1:
```
Ввод: nums = [1,2,3,1]
Вывод: true
```
Пример 2:
```
Ввод: nums = [1,2,3,4]
Вывод: false
```
Пример 3:

```
Ввод: nums = [1,1,1,3,3,4,3,2,4,2]
Вывод: true
```

'''
mas=[1,2,3]
for index1 in range(len(mas)):
    count=0
    for index2 in range(len(mas)):
        if mas[index1]==mas[index2]:
            count+=1
    if count>=2:
        print('True')

mas2=[1,2,3]
set1=set(mas2)
set2=set()
for index1 in range(len(mas2)):
    if mas2[index1] in set2:
        print('True')
    else:
        set2.add(mas2[index1])

print("asd")