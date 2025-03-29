# Даны два целочисленных массива nums1 и nums2, верните их пересечение.
# Каждый элемент в результате должен появляться столько раз, сколько он есть в обоих массивах.
# Вернуть результат можно в любом порядке.

nums1 = [1,2,2,1]
nums2 = [2,2, 1]
# [2,2]

dict1 = {}
dict2 = {}

for number in nums1:
    dict1[number] = dict1.get(number, 0) + 1
# print(dict1)
for number in nums2:
    dict2[number] = dict2.get(number, 0) + 1
result = []
for key in dict1.keys():
    count1 = dict1[key]
    count2 = dict2.get(key, 0)

    result_count = min(count1, count2)

    for _ in range(result_count):
        result.append(key)
print(result)
